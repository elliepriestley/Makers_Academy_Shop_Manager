from lib.database_connection import DatabaseConnection
from lib.item import Item

class ItemRepository():
    def __init__(self, connection):
        self.connection = connection

    def all(self):
        rows = self.connection.execute("SELECT * FROM items")
        items = []
        for row in rows:
            item = Item(row["id"], row["unit_price"], row["name"], row["quantity"])
            items.append(item)
        return items
    
    def create(self, item):
        self.connection.execute("INSERT INTO items (unit_price, name, quantity) VALUES (%s, %s, %s)", [item.unit_price, item.name, item.quantity])
        