class ContactBook:
    def __init__(self, file_name="contacts.txt"):
        self.file_name = file_name
        self.contacts = {}
        self.load_contacts()

    def add_contact(self, name, email, phone, address):
        if phone in self.contacts:
            print("Error: Phone number already exists.")
            return
        self.contacts[phone] = {"Name": name, "Email": email, "Address": address}
        self.save_contacts()
        print(f"Contact for {name} added successfully!")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
            return
        print("\nContacts List:")
        for phone, details in self.contacts.items():
            print(f"Phone: {phone}, Name: {details['Name']}, Email: {details['Email']}, Address: {details['Address']}")

    def remove_contact(self, phone):
        if phone in self.contacts:
            del self.contacts[phone]
            self.save_contacts()
            print("Contact removed successfully.")
        else:
            print("Error: Contact not found.")

    def search_contact(self, query):
        results = [f"Phone: {phone}, Details: {details}" for phone, details in self.contacts.items() if query.lower() in str(details).lower()]
        if results:
            print("\nSearch Results:")
            for result in results:
                print(result)
        else:
            print("No matching contacts found.")

    def load_contacts(self):
        try:
            with open(self.file_name, "r") as file:
                for line in file:
                    phone, name, email, address = line.strip().split(",")
                    self.contacts[phone] = {"Name": name, "Email": email, "Address": address}
        except FileNotFoundError:
            pass

    def save_contacts(self):
        with open(self.file_name, "w") as file:
            for phone, details in self.contacts.items():
                file.write(f"{phone},{details['Name']},{details['Email']},{details['Address']}\n")
