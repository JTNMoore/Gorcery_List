#defining item class of item name, section, and store
class Item:
    def __init__ (self, name, section, store):
        self.name = name
        self.section = section
        self.store = store
        
    def list_item(self):
        print(self.name + " -- " + self.store + " -- " + self.section)
