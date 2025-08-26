import random
import string

def password_generator(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

length = int(input("Enter the length of the password: "))

print(f"Generated Password: {password_generator(length)}")


#OUTPUT

/WindowsApps/python3.13.exe" "c:/Users/Janakiraman B/Downloads/Udemy Certificates/Projects/python mini projects/PasswordGenerator.py"
Enter the length of the password: 13
Generated Password: +uzw==3Whgug

Enter the length of the password: 13
Generated Password: 64vgu=3WPnd45

Enter the length of the password: 13
Generated Password: 00uij=3WPnd45

Enter the length of the password: 13
Generated Password: +uzw==fyvgvjb

Enter the length of the password: 13
Generated Password: +uzw==35767vb


