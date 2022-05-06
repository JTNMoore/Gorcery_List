import actions as a
import item_database as id

def main():
    print("Press 'Q' to quit or select from  the following options:")
    id.create_database()
    #user input to determine action
    while True:
        action = input("'C' to create new list\n'V' to view list\n'A' to add to list\n'D' to delete from list\n'E' To edit item in list: ")
        #If user enters Q or q quit program
        if action.lower() == 'c':
            a.create_list(input("Please enter a name for the new list: "))
        if action.lower() == 'a':
            a.add_to(input("Please enter the name of the list you would like to add to: "))
        elif action.lower() == 'q':
            return print("Thank you!")


main()
