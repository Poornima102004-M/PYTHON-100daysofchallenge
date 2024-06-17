contacts = {}

def add_contact(name, phone_number):
    """Add a contact to the contacts dictionary."""
    contacts[name] = phone_number
    print(f"Contact '{name}' added with phone number '{phone_number}'.")

def view_contacts():
    """View all contacts in the contacts dictionary."""
    if contacts:
        print("Contacts:")
        for name, phone_number in contacts.items():
            print(f"{name}: {phone_number}")
    else:
        print("No contacts found.")

def search_contact(name):
    """Search for a contact by name."""
    if name in contacts:
        print(f"Contact '{name}' found with phone number '{contacts[name]}'")
    else:
        print(f"Contact '{name}' not found.")

def delete_contact(name):
    """Delete a contact by name."""
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted successfully.")
    else:
        print(f"Contact '{name}' not found in the contacts list.")

def show_menu():
    """Display the menu options."""
    print("\nMenu:")
    print("1. Add a contact")
    print("2. View all contacts")
    print("3. Search for a contact")
    print("4. Delete a contact")
    print("5. Quit")

# Main program loop
while True:
    show_menu()
    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        name = input("Enter contact name: ")
        phone_number = input("Enter phone number: ")
        add_contact(name, phone_number)
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        name = input("Enter contact name to search: ")
        search_contact(name)
    elif choice == '4':
        name = input("Enter contact name to delete: ")
        delete_contact(name)
    elif choice == '5':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 5.")
