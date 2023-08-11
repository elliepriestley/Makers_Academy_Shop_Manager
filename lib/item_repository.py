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
        
    # def find_by_order(self, order_id):
    #     rows = self.connection.execute("SELECT (items.id, items.unit_price, items.name, items.quantity) FROM items JOIN items_orders ON items_orders.item_id = items.id JOIN orders ON orders.id = items_orders.order_id WHERE orders.id = %s" , [order_id])
    #     items = []
    #     for row in rows:
    #         print(row)
    #         item = Item(row['row'][0], row['row'][1], row['row'][2], row['row'][3])
    #         print(item)
    #         items.append(item)
    #     return items
            
