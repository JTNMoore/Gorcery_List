import actions as a

def main():
    print("Press 'Q' to quit or select from  the following options:")
    #user input to determine action
    while True:
        action = input("'C' to create new list\n'V' to view list\n'A' to add to list\n'D' to delete from list\n'E' To edit item in list: ")
        #If user enters Q or q quit program
        if action.lower() == 'c':
            a.create_list(input("Please enter a list name: "))
        elif action.lower() == 'q':
            return print("Thank you!")


main()
