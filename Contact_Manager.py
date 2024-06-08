from Contact import Contact


class ContactManager:
    
    contacts = [Contact(name='AFANA', phone='774931623',email='jeovany.afana50@gmail.com')]  # Liste que nous allons utiliser pour garder les contacts
    update_options_menu = \
        '''
         \t\t\t\t\tHOW DO YOU WANT TO UPDATE YOUR CONTACT?
         \ta- Update name
         \tb- Update phone number
         \tc- Update email
         '''
    if_contact_found = False

    def __init__(self):
        self.contact = Contact()
        self.contact_name = ''
        self.contact_email = ''
        self.contact_phone_number = ''

    def add_contact(self):
        self.contact_name = input('Enter contact name please: \n').upper()
        self.contact_phone_number = input('Enter contact phone number please: \n').upper()
        self.contact_email = input('Enter contact email please: \n').upper()

        self.contact = Contact(self.contact_name, self.contact_email, self.contact_phone_number)

        self.contacts.append(Contact(self.contact_name, self.contact_phone_number, self.contact_email))  #Ajout du nouveau contact à la liste des contacts
        print('Contact added successfully!')

    def show_saved_contacts(self):
        if len(self.contacts) == 0:
            print('No contacts saved!')

        print('\t' * 4 + 'List of contacts')
        for row in self.contacts:
            print(f'Contact name: {row.get_name()}')
            print(f'Contact phone number: {row.get_phone()}')
            print(f'Contact email: {row.get_email()}'+'\n\n')

    @staticmethod
    def search_contact(contact_name: str = None) -> None:  #Method who lets me search one specified contact in the list
        searched_contact = None
        local_contact_name = ''
        if contact_name is None:  #Condition who let me know if the method doesn't have any parameter
            contact_name = input('Enter contact name please: \n')
            local_contact_name = contact_name

        else:
            local_contact_name = contact_name

        for contact in ContactManager.contacts:
            if contact.get_name() == local_contact_name:
                searched_contact = contact
                ContactManager.if_contact_found = True
                break

        if searched_contact is None:
            print('Contact not found!')

        else:
            print('Contact found successfully!')

    @staticmethod
    def delete_contact(contact_name: str = None):
        if contact_name is None:
            contact_name = input('Enter contact name please: \n')

        for contact in ContactManager.contacts:
            if contact.get_name() == contact_name:
                ContactManager.contacts.remove(contact)
                print('Contact deleted successfully!')

    @staticmethod
    def update_contact(contact_name: str = None):
        local_name = ''
        if contact_name is None:
            contact_name = input('Enter contact name please: \n')
            local_name = contact_name
        else:
            local_name = contact_name
        ContactManager.search_contact(contact_name=local_name)

        if ContactManager.if_contact_found:
            print(ContactManager.update_options_menu)
            choice = input('>').strip()

            if choice.lower() == 'a':
                for contact in ContactManager.contacts:
                    if contact.get_name() == contact_name:
                        new_contact_name = input('Enter the new name please: \n')
                        contact.name_set(new_contact_name)
                        print('Contact name updated successfully!')

            elif choice.lower() == 'b':
                for contact in ContactManager.contacts:
                    if contact.get_name() == contact_name:
                        new_contact_phone = input('Enter the new phone number please: \n')
                        contact.phone_set(new_contact_phone)
                        print('Contact phone number updated successfully!')

            elif choice.lower() == 'c':
                for contact in ContactManager.contacts:
                    if contact.get_name() == contact_name:
                        new_contact_email = input('Enter the new email please: \n')
                        contact.email_set(new_contact_email)
                        print('Contact email updated successfully!')

            else:
                print('Choose an correct option please !')

    @staticmethod
    def save_contacts_in_text_file():
        with open('contacts.txt', 'w') as file:
            for contact in ContactManager.contacts:
                file.write(contact.get_name().upper()+' '+contact.get_phone()+' '+contact.get_email()+'\n')

    @staticmethod
    def load_contacts_from_text_file():
        current_line = None
        with open('contacts.txt', 'r') as file:
            for line in file:
                current_line = line.strip().split()
                ContactManager.contacts.append(Contact(current_line[0].upper(), current_line[1], current_line[2]))

                print('Contact saved successfully!')








