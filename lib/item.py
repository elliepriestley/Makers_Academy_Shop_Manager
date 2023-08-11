class Item():
    def __init__(self, id, unit_price, name, quantity):
        self.id = id
        self.unit_price = unit_price
        self.name = name
        self.quantity = quantity

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"Item({self.id}, {self.unit_price}, {self.name}, {self.quantity})"