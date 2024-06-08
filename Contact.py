class Contact:
    def __init__(self, name: str = None, phone: str = None, email: str = None):
        self.name = name
        self.phone = phone
        self.email = email

    def name_set(self, name) -> None:
        self.name = name

    def get_name(self):
        return self.name

    def phone_set(self, phone) -> None:
        self.phone = phone

    def get_phone(self):
        return self.phone

    def email_set(self, email) -> None:
        self.email = email

    def get_email(self):
        return self.email

    def show_contact_details(self):
        print("Name: " + self.name)
        print("Phone: " + self.phone)
        print("Email: " + self.email)

    def update_contact_name(self, name: str) -> None:
        self.name_set(name)
        print('Name updated successfully')

    def update_contact_phone(self, phone: str) -> None:
        self.phone_set(phone)
        print('Phone updated successfully')

    def update_contact_email(self, email: str) -> None:
        self.email_set(email)
        print('Email updated successfully')

