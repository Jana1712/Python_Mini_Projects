contacts = {}

def add_contact(name, phone):
    contacts[name] = phone

def view_contacts():
    for name, phone in contacts.items():
        print(f"{name}: {phone}")

while True:
    choice = input("1. Add Contact 2. View Contacts 3. Quit: ")
    if choice == '1':
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        add_contact(name, phone)
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        break
    else:
        print("Invalid choice!")