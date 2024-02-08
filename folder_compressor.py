# This is a dummay code for now

import os
import shutil
import tarfile
import zipfile

def compress_folder(folder_path, compress_type):
    folder_name = os.path.basename(folder_path)
    output_filename = f"{folder_name}_{date_today()}.{compress_type}"
    try:
        if compress_type == 'zip':
            with zipfile.ZipFile(output_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
                for root, dirs, files in os.walk(folder_path):
                    for file in files:
                        zipf.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), folder_path))
            print(f"Folder '{folder_name}' compressed successfully as '{output_filename}'.")
        elif compress_type == 'tar':
            with tarfile.open(output_filename, 'w') as tarf:
                tarf.add(folder_path, arcname=os.path.basename(folder_path))
            print(f"Folder '{folder_name}' compressed successfully as '{output_filename}'.")
        elif compress_type == 'tgz':
            with tarfile.open(output_filename, 'w:gz') as tarf:
                tarf.add(folder_path, arcname=os.path.basename(folder_path))
            print(f"Folder '{folder_name}' compressed successfully as '{output_filename}'.")
        else:
            print("Unsupported compression type.")
    except Exception as e:
        print(f"Compression failed: {e}")

def date_today():
    import datetime
    today = datetime.date.today()
    return today.strftime("%Y_%m_%d")

def main():
    folder_path = input("Enter the path of the folder to compress: ").strip()
    if not os.path.exists(folder_path):
        print("Folder does not exist.")
        return

    print("Available compressed file types:")
    print("1. zip")
    print("2. tar")
    print("3. tgz")

    compress_type = input("Select the desired compressed file type: ").strip().lower()

    if compress_type not in ['zip', 'tar', 'tgz']:
        print("Invalid compression type.")
        return

    compress_folder(folder_path, compress_type)

if __name__ == "__main__":
    main()
