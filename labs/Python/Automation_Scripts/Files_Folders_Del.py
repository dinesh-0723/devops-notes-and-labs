import os, shutil

# Folders to clean
#paths = [r"C:\Users\XYZ\AppData\Local\Temp", r"C:\Windows\Temp"]
paths = [r"C:\Users\XYZ\AppData\Local\Temp"]

for path in paths:
    print(f"Cleaning: {path}")
    if os.path.exists(path):
        for item in os.listdir(path):
            item_path = os.path.join(path, item)
            try:
                if os.path.isfile(item_path) or os.path.islink(item_path):
                    os.unlink(item_path)       # Delete files
                elif os.path.isdir(item_path):
                    shutil.rmtree(item_path)   # Delete folders
            except Exception as e:
                print(f"Cannot delete {item_path}: {e}")

print("\nCleanup completed successfully.")