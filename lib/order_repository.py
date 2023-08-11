from lib.order import Order

class OrderRepository():
    def __init__(self, connection):
        self.connection = connection

    def all(self):
        rows = self.connection.execute("SELECT * FROM orders")
        orders = []
        for row in rows:
            order = Order(row["id"], row["customer_name"], row["order_date"])
            orders.append(order)
        return orders
    
    def create(self, order):
        self.connection.execute("INSERT INTO orders (customer_name, order_date) VALUES (%s, %s)", [order.customer_name, order.order_date])

    def find_by_item(self, item):
        rows = self.connection.execute("SELECT orders.id, orders.customer_name, orders.order_date FROM orders JOIN items_orders ON items_orders.order_id = orders.id JOIN items ON items.id = items_orders.item_id WHERE items.id = %s", [item])
        orders = []
        for row in rows:
            order = Order(row["id"], row["customer_name"], row["order_date"])
            print(order)
            orders.append(order)
        return orders
