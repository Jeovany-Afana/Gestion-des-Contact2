from Contact_Manager import ContactManager
import sys as system


class Application:
    def __init__(self, user_choice: int = None):
        self.choice = user_choice
        self.contactManager = ContactManager()
        self.operations = \
            {
                1: self.contactManager.add_contact,
                2: self.contactManager.show_saved_contacts,
                3: self.contactManager.search_contact,
                4: self.contactManager.delete_contact,
                5: self.contactManager.update_contact,
                6: self.contactManager.save_contacts_in_text_file,
                7: self.contactManager.load_contacts_from_text_file,
                8: system.exit,
            }

    def execute_operation(self, precice_choice: int = None):  # Méthode qui permet de lancer les opération du programme en fonction du choix de l'utilisateur
        if precice_choice is not None and precice_choice in self.operations:
            self.operations[precice_choice]()

        else:
            self.operations[self.choice]()  #Au cas où on appelle la méthode sans passer un paramètre



