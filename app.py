from lib.database_connection import DatabaseConnection
from lib.order_repository import OrderRepository
from lib.item_repository import ItemRepository
from lib.item import Item
from lib.order import Order


class Application():
    def __init__(self):
        self.connection = DatabaseConnection()
        self.connection.connect()
        self.connection.seed("seeds/items_orders.sql")

    def run(self):
        print('Welcome to the shop management program!')
        print('What would you like to do?')
        print(' * 1 - List all shop items \n * 2 - Create a new shop item \n * 3 - List all orders \n * 4 - Create a new order ')
        user_input = int(input())
        if user_input == 1:
            print('Here is a list of all shop items:')
            repository = ItemRepository(self.connection)
            items = repository.all()
            for item in items:
                print(f"#{item.id} Name: {item.name}, Unit Price: {item.unit_price}, Quantity: {item.quantity}")
        elif user_input == 2:
            print('Please enter the new item you would like to create...')
            print('What is the item unit price?')
            input_unit_price = float(input())
            print('Thank you. What is the item name?')
            input_name = str(input())
            print('Thank you. Finally, what is the item quantity?')
            input_quantity = int(input())
            new_item = Item(None, input_unit_price, input_name, input_quantity)
            repository = ItemRepository(self.connection)
            repository.create(new_item)
            print("New item created, please find the new item listed below:")
            items = repository.all()
            for item in items:
                print(f"#{item.id} Name: {item.name}, Unit Price: {item.unit_price}, Quantity: {item.quantity}")
        elif user_input == 3:
            print('Here is a list of all orders:')
            repository = OrderRepository(self.connection)
            orders = repository.all()
            for order in orders:
                print(f"#{order.id} Customer Name: {order.customer_name}, Order Date: {order.order_date}")
        elif user_input == 4:
            print('Please enter the new order you would like to create...')
            print('What is the customer name?')
            input_customer_name = str(input())
            print('Thank you. What is the order date?')
            input_order_date = str(input())
            new_order = Order(None, input_customer_name, input_order_date)
            repository = OrderRepository(self.connection)
            repository.create(new_order)
            print("New order created, please find the new order listed below:")
            orders = repository.all()
            for order in orders:
                print(f"#{order.id} Customer Name: {order.customer_name}, Order Date: {order.order_date}")
        else:
            print("Invalid input, please enter a number prompt between 1 - 4")
            app.run()









if __name__ == '__main__':
    app = Application()
    app.run()