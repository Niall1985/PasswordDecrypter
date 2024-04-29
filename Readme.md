## PDF Password Decrypter
This Python script is designed to decrypt passwords for PDF files using a brute-force approach. It generates potential passwords and attempts to decrypt the PDF file until the correct password is found or the specified password length range is exhausted.

Prerequisites
Python 3.x
PyPDF2 library
Itertools library

#Installation
Clone or download the repository to your local machine.
Install the required libraries by running:

#Copy code
pip install PyPDF2
Itertools comes pre-installed

#Usage
Open the script (pdf_password_cracker.py) in your preferred text editor.
Set the pdf_path variable to the file path of the PDF document you want to decrypt.
Set the min_length and max_length variables to specify the desired password length range.
Run the script using the following command:
Copy code
python pdf_password_cracker.py

#Customization
You can adjust the character set used for password generation by modifying the chars variable in the generate_passwords function.
The progress_interval variable in the crack_password function controls how often progress updates are printed. Adjust this value according to your preference.

#Disclaimer
This script is provided for educational purposes only. Attempting to decrypt passwords without proper authorization may be illegal and unethical. Use this script responsibly and only on PDF files for which you have explicit permission to decrypt the passwords.
