# PDF Password Decrypter
This Python script is designed to decrypt passwords for PDF files using a brute-force approach. It generates potential passwords and attempts to decrypt the PDF file until the correct password is found or the specified password length range is exhausted.

## Prerequisites
1. Python 3.x
2. PyPDF2 library
3. Itertools library

## Installation
1. Clone or download the repository to your local machine.
2. Install the required libraries by running:

## Copy code
1. pip install PyPDF2.
2. Itertools comes pre-installed.

## Usage
1. Open the script (pdf_password_cracker.py) in your preferred text editor.
2. Set the pdf_path variable to the file path of the PDF document you want to decrypt.
3. Set the min_length and max_length variables to specify the desired password length range.
4. Run the script using the following command:
5. Copy code
6. python pdf_password_cracker.py

## Customization
You can adjust the character set used for password generation by modifying the chars variable in the generate_passwords function.
The progress_interval variable in the crack_password function controls how often progress updates are printed. Adjust this value according to your preference.

## Disclaimer
This script is provided for educational purposes only. Attempting to decrypt passwords without proper authorization may be illegal and unethical. Use this script responsibly and only on PDF files for which you have explicit permission to decrypt the passwords.
