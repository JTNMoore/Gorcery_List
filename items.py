#defining item class of item name, section, and store
class Item:
    def __init__ (self, name, section, store, quantity):
        self.name = name
        self.section = section
        self.store = store
        self.quantity = quantity
        
    def list_item(self):
        print(self.name + " x" + self.quantity + " -- " + self.store + " -- " + self.section)
