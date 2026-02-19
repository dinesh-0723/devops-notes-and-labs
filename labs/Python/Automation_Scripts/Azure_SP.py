import requests
from azure.identity import AzureCliCredential
from datetime import datetime, timedelta

# Authenticate using Azure CLI login
credential = AzureCliCredential()
token = credential.get_token("https://graph.microsoft.com/.default")

headers = {
    "Authorization": f"Bearer {token.token}"
}

url = "https://graph.microsoft.com/v1.0/applications?$select=displayName,appId,passwordCredentials"

#threshold = datetime.utcnow() + timedelta(days=30)
from datetime import datetime, timedelta, UTC

threshold = datetime.now(UTC) + timedelta(days=30)
print(threshold)

print("\n🔎 Expiring Secrets Report\n")

while url:
    response = requests.get(url, headers=headers)
    data = response.json()

    for app in data.get("value", []):
        display_name = app.get("displayName")
        app_id = app.get("appId")

        for cred in app.get("passwordCredentials", []):
            end_date = cred.get("endDateTime")

            if end_date:
                expiry = datetime.fromisoformat(end_date.replace("Z", "+00:00"))

                if expiry < threshold:
                    print(f"⚠️ Expiring Soon")
                    print(f"Display Name : {display_name}")
                    print(f"Client ID    : {app_id}")
                    print(f"Tenant ID    : Retrieved from login")
                    print(f"Expires On   : {expiry}")
                    print("-" * 60)

    url = data.get("@odata.nextLink")