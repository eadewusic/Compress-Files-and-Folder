# Folder Compressor

## Table of Contents

- [Description](#description)
- [Requirements](#requirements)
- [Usage](#usage)
- [Example](#example)
- [Group Members](#group-members)

## Description

This Python program allows users to compress files and folders to various compressed file types, including `.zip`, `.tar`, and `.tgz`. It provides a simple command-line interface for selecting the folder to compress and the desired compression type. If the user selects `.tgz` as the compression type, the program automatically names the compressed file with the convention `name_of_the_folder_date_month_year.tgz`.

## Requirements

- Python 3.x
- Required libraries: `os`, `shutil`, `tarfile`, `zipfile`

## Usage

1. Clone or download this repository to your local machine.
2. Navigate to the directory containing the `folder_compressor.py` file using the command line.
3. Run the program by executing the following command:
   ```
   python folder_compressor.py
   ```
4. Follow the prompts to provide the path of the folder you want to compress and select the desired compression type.

## Example

Suppose you have a folder named `MyFolder` located at `C:\Users\Username\Documents\MyFolder`. You want to compress this folder into a `.tgz` file. Here's how you would use the program:

1. Run the program by executing `python folder_compressor.py`.
2. Enter the path `C:\Users\Username\Documents\MyFolder` when prompted for the folder path.
3. Choose `tgz` as the compression type.
4. The compressed file will be saved as `MyFolder_<current_date>.tgz` in the same directory where the program is run.

## Group Members

- Eunice Adewusi (Climiradi) <e.adewusi@alustudent.com>
- Emmanuel Obolo <e.obolo@alustudent.com>
- Ola-Adisa Shobi <s.olaadisa@alustudent.com>
- Purity Kihiu <p.kihiu@alustudent.com>
- Pascal Mugisha <p.mugisha@alustudent.com>
