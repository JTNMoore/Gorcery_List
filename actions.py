Stores = ["Target", "Trader Joes", "Walmart", "Other"]
Sections = ["Appliances", "Automotive", "Clothing", "Deli", "Electronics", "Home", "Produce", "Toys", "Video Games", "Other", "Return"]

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
        print_list(Stores)
        #user input for store name
        store_int = input("Enter the number for the store you want to make a list for or 'Q' to quit: ")
        if store_int.lower() == 'q':
            #end function and print out list created
            print_list(list_name)
            return
        #store name value
        store = Stores[int(store_int) - 1]
        section_int = 0
        #loop while section is not return
        while section_int != 11:
            print_list(Sections)
            #user input for sections
            section_int = int(input("\nEnter the number for the section the item can be found in from the above list or '11' to return to Store list: "))
            section = Sections[section_int - 1]
            name = ""
            #if not return continue adding items
            if section_int != 11:
                while name.lower() != "r":
                    #user input for item names
                    name = input("Enter the items you would like to add to the list or type 'R' to return to Section list: ")
                    #if entry is not blank or q add it to the list
                    if name and name.lower() != "r":
                        new_item = Item(name, section, store)
                        list_name.append(new_item)
                    
        
def print_list(list):
    if list == Stores or list == Sections:
        n = 1
        for s in list:
            print(str(n) + ". " + s + " -- ", end = '')
            n += 1
    else:
        for i in list:
            i.list_item()
