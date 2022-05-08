import actions as a
import item_database as id

def main():
    print("Press 'Q' to quit or select from  the following options:")
    id.create_database()
    #user input to determine action
    while True:
        action = input("'C' to create new list\n'V' to view lists\n'A' to add to list\n'D' to delete from list\n'E' To edit item in list: ")
        #If user enters c to create list
        if action.lower() == 'c':
            a.create_list(input("Please enter a name for the new list: "))
        #user enters a to add to list
        elif action.lower() == 'a':
            a.add_to(input("Please enter the name of the list you would like to add to: "))
        #user enters v to view lists
        elif action.lower() == 'v':
            #call to view lists in database
            id.view_lists()
        #developer only
        elif action.lower() == "clear all":
            #clear all tables
            id.delete_table()
            #recreate database
            id.create_database()
        #if user enters Q or q quit program
        elif action.lower() == 'q':
            return print("Thank you!")


main()
