from items import Item

def create_list(list_name):
    #create a new list using user input
    list_name = []
    #calling 'add_to' function to populate new list
    add_to(list_name)
    #end function
    return
    
            
def add_to(list_name):
    list_name = []
    #continue looping until the user quits
    while True:
        #user input for store name
        store = input("Enter the name for the store you want to make a list for or 'R' to return: ")
        if store.lower() == "r":
            #end function and print out list created
            print_list(list_name)
            return
        #store name value
        #loop while section is not return
        section = ""
        while section.lower() != "r":
            #user input for sections
            section = input("Enter the name for the section the item can be found in or 'R' to return to Store list: ")
            name = ""
            #if not return continue adding items
            if section != "r":
                while name.lower() != "r":
                    #user input for item names
                    name = input("Enter the items you would like to add to the list or type 'R' to return to Section list: ")
                    #if entry is not blank or q add it to the list
                    if name and name.lower() != "r":
                        new_item = Item(name, section, store)
                        list_name.append(new_item)
                    
        
def print_list(list):
    for i in list:
        i.list_item()
