from items import Item
from operator import attrgetter
import item_database as id

#this function creates a new list and then call the add_to function to add items
def create_list(list_name):
    id.add_list(list_name)
    #calling 'add_to' function to populate new list
    add_to(list_name)
    #end function
    return
    

#this function adds items to a list
def add_to(list_name):
    item_list = []
    #continue looping until the user quits
    while True:
        #user input for store name
        store = input("Enter the name for the store you want to make a list for or 'R' to return: ")
        if store.lower() == "r":
            #end function and print out list created
            item_list.sort(key=attrgetter('store', 'section', 'name'))
            print(list_name)
            print_list(list_name, item_list)
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
                        quantity = input("How many of this item are needed:")
                        new_item = Item(name, section, store, quantity)
                        item_list.append(new_item)
                    

#this function prints the items in the list using the class function list_item and add them to the item_lists file
def print_list(name, list):
    for i in list:
        i.list_item()
    return

