# import os
# import shutil

# work_path = r"C:\Users\XYZ\Desktop\Klock"

# for folder in os.listdir(work_path):
#     folder_path = os.path.join(work_path, folder)

#     # check if folder name is a number (1,2,3...)
#     if os.path.isdir(folder_path) and folder.isdigit():
#         try:
#             #shutil.rmtree(folder_path)
#             print(f"Deleted: {folder_path}")
#         except Exception as e:
#             print(f"Error deleting {folder_path}: {e}")

import os
import shutil

work_path = r"C:\Users\XYZ\Desktop\Klock"

# Function to get C: drive usage
def get_c_drive_usage():
    usage = shutil.disk_usage("C:\\")
    used_gb = usage.used / (1024**3)
    free_gb = usage.free / (1024**3)
    total_gb = usage.total / (1024**3)
    return total_gb, used_gb, free_gb

# Check C: drive before deletion
total_before, used_before, free_before = get_c_drive_usage()
print(f"C: Drive before deletion - Total: {total_before:.2f} GB, Used: {used_before:.2f} GB, Free: {free_before:.2f} GB\n")

for folder in os.listdir(work_path):
    folder_path = os.path.join(work_path, folder)

    # check if folder name is a number (1,2,3...)
    if os.path.isdir(folder_path) and folder.isdigit():
        try:
            # Uncomment the next line to actually delete
            shutil.rmtree(folder_path)
            print(f"Deleted: {folder_path}")
        except Exception as e:
            print(f"Error deleting {folder_path}: {e}")

# Check C: drive after deletion
total_after, used_after, free_after = get_c_drive_usage()
print(f"\nC: Drive after deletion - Total: {total_after:.2f} GB, Used: {used_after:.2f} GB, Free: {free_after:.2f} GB")