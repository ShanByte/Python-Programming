def display_contacts(contacts):
    if not contacts:
        print("No contacts yet!")
        return
    
    print("\nYour Contacts:")
    for name, phone in contacts.items():
        print(f"{name}: {phone}")

def main():
    contacts = {}
    
    while True:
        print("\nContact Book")
        print("1. Add contact")
        print("2. View contacts")
        print("3. Search contact")
        print("4. Delete contact")
        print("5. Exit")
        
        choice = input("\nChoose option: ")
        
        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            contacts[name] = phone
            print("Contact added!")
        
        elif choice == '2':
            display_contacts(contacts)
        
        elif choice == '3':
            name = input("Enter name to search: ")
            if name in contacts:
                print(f"{name}: {contacts[name]}")
            else:
                print("Contact not found!")
        
        elif choice == '4':
            name = input("Enter name to delete: ")
            if name in contacts:
                del contacts[name]
                print("Contact deleted!")
            else:
                print("Contact not found!")
        
        elif choice == '5':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()