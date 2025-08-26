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



# OUTPUT

1. Add Contact 2. View Contacts 3. Quit: 1
Enter name: jana
Enter phone number: 9962404206
1. Add Contact 2. View Contacts 3. Quit: 2
jana: 9962404206
1. Add Contact 2. View Contacts 3. Quit: 1
Enter name: suresh
Enter phone number: 8925406765  
1. Add Contact 2. View Contacts 3. Quit: 2
jana: 9962404206
suresh: 8925406765
1. Add Contact 2. View Contacts 3. Quit:
jana: 9962404206
suresh: 8925406765
1. Add Contact 2. View Contacts 3. Quit:
jana: 9962404206
suresh: 8925406765
1. Add Contact 2. View Contacts 3. Quit:
jana: 9962404206
suresh: 8925406765
1. Add Contact 2. View Contacts 3. Quit:

