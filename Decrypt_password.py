import itertools
import PyPDF2

def generate_passwords(min_length=1, max_length=20):
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890_@#$&$!{]}[+-*/?><"
    for length in range(min_length, max_length + 1):
        passwords = itertools.product(chars, repeat=length)
        yield from ("".join(password) for password in passwords)
#the generate_passwords function generates passwords for testing using capital and small letters, numbers and special characters

def crack_password(pdf_path, min_length, max_length, progress_interval=10):
    pdf_reader = PyPDF2.PdfReader(open(pdf_path, "rb"))
    attempt_count = 0

#The for looop mentioned below iterates through each password length in the specified range
    for length in range(min_length, max_length + 1):
        potential_passwords = generate_passwords(length, length)
        #the following loop iterates through all the passwords generated to find the correct one
        for password in potential_passwords:
            password = password.strip() #removes leading and trailing whitespaces
            attempt_count += 1
            if attempt_count % progress_interval == 0:
                #displays an output of the ongoing decryption process
                print(f"Attempt {attempt_count}: Trying password '{password}'")
            if pdf_reader.decrypt(password) == 1:
                print(f"Password cracked: {password}")
                return password
    print("Password not found")
    return None

pdf_path = "" #add ythe filepath of the file whose passwords you wish to decrypt
min_length = 5 #specify your desired minimum password length
max_length = 10 #specify your desired maximum password length range
crack_password(pdf_path, min_length,max_length)
