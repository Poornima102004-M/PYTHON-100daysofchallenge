import pickle
import os

class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

class AddressBook:
    def __init__(self, filename):
        self.filename = filename
        self.contacts = []
        self.load_contacts()

    def load_contacts(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'rb') as file:
                self.contacts = pickle.load(file)

    def save_contacts(self):
        with open(self.filename, 'wb') as file:
            pickle.dump(self.contacts, file)

    def add_contact(self, name, phone):
        contact = Contact(name, phone)
        self.contacts.append(contact)
        self.save_contacts()

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                self.save_contacts()
                print(f"Deleted contact: {name}")
                return
        print(f"Contact '{name}' not found.")

    def list_contacts(self):
        if self.contacts:
            print("Address Book:")
            for contact in self.contacts:
                print(f"{contact.name}: {contact.phone}")
        else:
            print("Address Book is empty.")

# Function to display menu and handle user input
def main_menu(address_book):
    while True:
        print("\nMenu:")
        print("1. Add Contact")
        print("2. Delete Contact")
        print("3. List Contacts")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            address_book.add_contact(name, phone)
        elif choice == '2':
            name = input("Enter name to delete: ")
            address_book.delete_contact(name)
        elif choice == '3':
            address_book.list_contacts()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

if __name__ == "__main__":
    address_book = AddressBook("contacts.pickle")
    main_menu(address_book)
