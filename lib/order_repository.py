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