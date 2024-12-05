from contact_book import ContactBook
from utilities import validate_string, validate_phone

def main():
    contact_book = ContactBook()
    while True:
        print("\nContact Book Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Remove Contact")
        print("4. Search Contacts")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            try:
                name = validate_string(input("Enter Name: "), "Name")
                email = validate_string(input("Enter Email: "), "Email")
                phone = validate_phone(input("Enter Phone Number: "))
                address = validate_string(input("Enter Address: "), "Address")
                contact_book.add_contact(name, email, phone, address)
            except ValueError as e:
                print(f"Error: {e}")
        
        elif choice == "2":
            contact_book.view_contacts()
        
        elif choice == "3":
            phone = input("Enter Phone Number to remove: ")
            contact_book.remove_contact(phone)
        
        elif choice == "4":
            query = input("Enter search query (name, email, or address): ")
            contact_book.search_contact(query)
        
        elif choice == "5":
            print("Exiting... Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
