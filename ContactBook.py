class Contact:
    def __init__(self, name, phone_number, email):
        self.name = name
        self.phone_number = phone_number
        self.email = email

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self):
        name = input("Enter contact name: ")
        phone_number = input("Enter contact phone number: ")
        email = input("Enter contact email: ")
        contact = Contact(name, phone_number, email)
        self.contacts.append(contact)
        print("Your Contact added successfully!")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts in the contact book.")
        else:
            for i, contact in enumerate(self.contacts, start=1):
                print(f"Contact {i}:")
                print(f"Name: {contact.name}")
                print(f"Phone Number: {contact.phone_number}")
                print(f"Email: {contact.email}")
                print()

    def search_contact(self):
        name = input("Enter contact name to search: ")
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                print(f"Name: {contact.name}")
                print(f"Phone Number: {contact.phone_number}")
                print(f"Email: {contact.email}")
                return
        print("Contact not found.")

    def delete_contact(self):
        name = input("Enter contact name to delete: ")
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                self.contacts.remove(contact)
                print("Contact deleted successfully!")
                return
        print("Contact not found.")

def main():
    contact_book = ContactBook()
    while True:
        print("Contact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Quit")
        choice = input("Enter your choice: ")
        if choice == "1":
            contact_book.add_contact()
        elif choice == "2":
            contact_book.view_contacts()
        elif choice == "3":
            contact_book.search_contact()
        elif choice == "4":
            contact_book.delete_contact()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()