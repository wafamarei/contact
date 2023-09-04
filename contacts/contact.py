import json

class Contact:
    def data(Id, name, phone, email):
        Id.name = name
        Id.phone = phone
        Id.email = email

class ContactFile:
    def data(Id):
        Id.contacts = []

    def _add(Id, contact):
        Id.contacts.append(contact)

    def _edit(Id, name, new_phone, new_email):
        for contact in Id.contacts:
            if contact.name == name:
                contact.phone = new_phone
                contact.email = new_email
                break

    def _delete(Id, name):
        Id.contacts = [contact for contact in Id.contacts if contact.name != name]

    def _search(Id, name):
        for contact in Id.contacts:
            if contact.name == name:
                return contact
        return None

    def _display(Id):
        for contact in Id.contacts:
            print(f"Name: {contact.name}, Phone: {contact.phone}, Email: {contact.email}")

    def SaveJson(Id, filename):
        data = []
        for contact in Id.contacts:
            data.append({"name": contact.name, "phone": contact.phone, "email": contact.email})
        with open(filename, "w") as file:
            json.dump(data, file)

    def LodeJson(Id, filename):
        try:
            with open(filename, "r") as file:
                data = json.load(file)
                for item in data:
                    contact = Contact(item["name"], item["phone"], item["email"])
                    Id.contacts.append(contact)
        except FileNotFoundError:
            pass

def main():
    contact_book = ContactFile()
    contact_book.LodeJson("contactsfile")

    while True:
        print("\n1- Add Contact\n2- Edit Contact\n3- Delete Contact\n4- Search Contact\n5- Display Contacts\n6- Save and Exit")
        choice = input(" Please Enter Your Choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            new_contact = Contact(name, phone, email)
            contact_book._add(new_contact)
        elif choice == '2':
            name = input("Enter name to edit: ")
            new_phone = input("Enter new phone number: ")
            new_email = input("Enter new email: ")
            contact_book._edit(name, new_phone, new_email)
        elif choice == '3':
            name = input("Enter name to delete: ")
            contact_book._delete(name)
        elif choice == '4':
            name = input("Enter name to search: ")
            found_contact = contact_book._search(name)
            if found_contact:
                print(f"Contact found - Name: {found_contact.name}, Phone: {found_contact.phone}, Email: {found_contact.email}")
            else:
                print("Contact not found.")
        elif choice == '5':
            contact_book._display()
        elif choice == '6':
            contact_book.SaveJson("contactsfile")
            break
        else:
            print("Wrong Choice. Please Select one number from 1 to 6.^^")

if __name__ == "__main__":
    main()

