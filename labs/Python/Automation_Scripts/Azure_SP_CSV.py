import requests
import csv
from azure.identity import AzureCliCredential
from datetime import datetime, timedelta, UTC

# -------------------------------
# CONFIGURATION
# -------------------------------
CSV_FILENAME = "expiring_secrets.csv"
DAYS_THRESHOLD = 30  # alert for secrets expiring within 30 days

# -------------------------------
# AUTHENTICATION
# -------------------------------
credential = AzureCliCredential()
token = credential.get_token("https://graph.microsoft.com/.default")

headers = {
    "Authorization": f"Bearer {token.token}"
}

# -------------------------------
# VARIABLES
# -------------------------------
url = "https://graph.microsoft.com/v1.0/applications?$select=displayName,appId,passwordCredentials"
threshold = datetime.now(UTC) + timedelta(days=DAYS_THRESHOLD)

expiring_secrets = []

# -------------------------------
# FETCH APPLICATIONS
# -------------------------------
while url:
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # fail fast if request fails
    data = response.json()

    for app in data.get("value", []):
        display_name = app.get("displayName")
        app_id = app.get("appId")

        for cred in app.get("passwordCredentials", []):
            end_date = cred.get("endDateTime")
            if end_date:
                expiry = datetime.fromisoformat(end_date.replace("Z", "+00:00"))
                if expiry < threshold:
                    expiring_secrets.append({
                        "Display Name": display_name,
                        "Client ID": app_id,
                        "Tenant ID": "",  # optional, can fetch dynamically
                        "Expires On": expiry.strftime('%Y-%m-%d %H:%M:%S %Z')
                    })

    url = data.get("@odata.nextLink")  # pagination

# -------------------------------
# EXPORT TO CSV
# -------------------------------
if expiring_secrets:
    with open(CSV_FILENAME, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["Display Name", "Client ID", "Tenant ID", "Expires On"])
        writer.writeheader()
        for item in expiring_secrets:
            writer.writerow(item)

    print(f"CSV exported to {CSV_FILENAME} with {len(expiring_secrets)} expiring secret(s).")
else:
    print(f"No secrets are expiring in the next {DAYS_THRESHOLD} days.")
