import os
import shutil
import tarfile
import zipfile
from datetime import datetime

def compress_folder(folder_path, compress_type):
    try:
        folder_name = os.path.basename(folder_path)
        current_date = datetime.now().strftime("%Y_%m_%d")
        compressed_file_name = f"{folder_name}_{current_date}.{compress_type}"

        if compress_type == 'zip':
            with zipfile.ZipFile(compressed_file_name, 'w') as zip_file:
                [zip_file.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), folder_path))
                 for root, _, files in os.walk(folder_path) for file in files]
        elif compress_type in ['tar', 'tgz']:
            with tarfile.open(compressed_file_name, f'w:{"gz" if compress_type == "tgz" else ""}') as tar_file:
                tar_file.add(folder_path, arcname=os.path.basename(folder_path))
        else:
            raise ValueError("Invalid compression type. Supported types: zip, tar, tgz")

        print(f"Compression successful. Compressed file saved as: {compressed_file_name}")
        return True

    except Exception as e:
        print(f"Compression failed. Error: {str(e)}")
        return False

def main():
    folder_path = input("Enter the path of the folder to compress: ")

    print("Available compressed file types: zip, tar, tgz")
    compress_type = input("Enter the desired compression type: ")

    if compress_type.lower() in {'zip', 'tar', 'tgz'}:
        compress_folder(folder_path, compress_type.lower())
    else:
        print("Invalid compression type. Please choose a valid option.")

if __name__ == "__main__":
    main()
