modules_to_check = [
    "flask",
    "psycopg2-binary",
    "sqlalchemy",
    "python-dotenv"
]

for module in modules_to_check:
    try:
        __import__(module)
        print(f"{module} ✅ Installed")
    except ImportError:
        print(f"{module} ❌ Not Installed")
