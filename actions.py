def create_list(list_name):
    list_name = []
    print("Enter 'Q' to quit")
    while True:
        item = input("Enter the items you would like to add to the list:")
        if item and item.lower() != 'q':
            list_name.append(item)
        elif item.lower() == 'q': 
            return print(list_name)
