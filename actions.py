Stores = ["Target", "Trader Joes", "Walmart", "Other"]
Sections = ["Appliances", "Automotive", "Closthing", "Deli", "Electronics", "Home", "Produce", "Toys", "Video Games", "Other", "Quit"]

from Items import Item

def create_list(list_name):
    #create a new list using user input
    list_name = []
    #calling 'add_to' function to populate new list
    add_to(list_name)
    #end function
    return
    
            
def add_to(list_name):
    list_name = []
    print_list(Stores)
    store_int = 0
    while True:
        while store_int >= 1 or store_int <= len(Stores):
            store_int = raw_input("Enter the number for the store you will be shopping at for this item or 'Q' to quit: ")
            if store_int.lower() == 'q':
                #end function and print out list created
                del new_item
                print_list(list_name)
                return
            store = Stores[store_int - 1]
            #making a list for a specific store
            print_list(Sections)
            section = input("Enter the number for the section the item can be found in from the above list or : ")
                while True:
                    name = input("Enter the items you would like to add to the list:")
                    #if entry is not blank or q add it to the list
                    if name and name.lower() != 'q':
                        new_item = Item(name, section, store)
                        list_name.append(new_item)
                    elif name.lower() == 'q':
                    
        
        
def print_list(list):
    if list == Stores or list == Sections:
        n = 1
        for s in list:
            print(str(n) + ". " + s + " -- ", end = '')
            n += 1
    else:
        for i in list:
            i.list_item()
