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
        print(' \n Welcome to the shop management program! \n \n What would you like to do? \n * 1 - List all shop items \n * 2 - Create a new shop item \n * 3 - List all orders \n * 4 - Create a new order \n * 5 - List all orders containing a particular item \n * 6 - List all items from a particular order ')
        user_input = int(input())
        if user_input == 1:
            print('Here is a list of all shop items:')
            items = (ItemRepository(self.connection)).all()
            for item in items:
                print(f"#{item.id} Name: {item.name}, Unit Price: {item.unit_price}, Quantity: {item.quantity}")
        elif user_input == 2:
            input_unit_price = float(input('Please enter the new item you would like to create... \n What is the item unit price?'))
            input_name = input('Thank you. What is the item name?')
            input_quantity = int(input('Thank you. Finally, what is the item quantity?'))
            new_item = Item(None, input_unit_price, input_name, input_quantity)
            repository = ItemRepository(self.connection)
            repository.create(new_item)
            print("New item created, please find the new item listed below:")
            items = repository.all()
            for item in items:
                print(f"#{item.id} Name: {item.name}, Unit Price: {item.unit_price}, Quantity: {item.quantity}")
        elif user_input == 3:
            print('Here is a list of all orders:')
            orders =  OrderRepository(self.connection).all()
            for order in orders:
                print(f"#{order.id} Customer Name: {order.customer_name}, Order Date: {order.order_date}")
        elif user_input == 4:
            input_customer_name = input('Please enter the new order you would like to create... \n What is the customer name?')
            input_order_date = input('Thank you. What is the order date?')
            new_order = Order(None, input_customer_name, input_order_date)
            OrderRepository(self.connection).create(new_order)
            print("New order created, please find the new order listed below:")
            orders = repository.all()
            for order in orders:
                print(f"#{order.id} Customer Name: {order.customer_name}, Order Date: {order.order_date}")
        elif user_input == 5:
            input_item_id = int(input("Please enter item id:"))
            print('The item is present in the following orders: \n')
            repository = OrderRepository(self.connection).find_by_item(input_item_id)
        elif user_input == 6:
            input_order_id =int(input("Please enter order id:"))
            print(f'The following items were included in order {input_order_id}: \n')
            repository = ItemRepository(self.connection).find_by_order(input_order_id)
        else:
            print("Invalid input, please enter a number prompt between 1 - 6")
            app.run()









if __name__ == '__main__':
    app = Application()
    app.run()