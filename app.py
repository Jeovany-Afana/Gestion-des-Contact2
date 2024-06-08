from app_manage import Application

menu =\
 '''
\t\t\t\t\tMAKE A CHOICE
\t1- Add a new contact
\t2- Show all saved contacts
\t3- Search for a contact by name or phone number
\t4- Delete a contact
\t5- Update information for an existing contact
\t6- Save a contact in a text file
\t7- Load the contact list from a text file
\t8- Exit
      Please make a choice
'''
while True:
    print(menu)
    choice = int(input('> ').strip())
    if choice == 8:
        print('Bye bye! 👋')  #Message to print if the user wants to quit the app

    app = Application(user_choice=choice)
    app.execute_operation()
    app.execute_operation(2)






