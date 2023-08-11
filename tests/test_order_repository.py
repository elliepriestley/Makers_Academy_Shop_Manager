from lib.database_connection import DatabaseConnection
from lib.order_repository import OrderRepository
from lib.order import Order

"""
Test all method returns list of all orders in orders table form database
"""


def test_all_method(db_connection):
    db_connection.seed("seeds/items_orders.sql")
    repository = OrderRepository(db_connection)
    assert repository.all() == [
        Order(1,'Ellie Priestley', '11-08-2023'),
        Order(2, 'Julian Vallender', '07-01-2023'),
        Order(3, 'Sarah Olivia', '09-06-2022'),
        Order(4, 'Finn Priestley', '09-09-2022'),
        Order(5, 'Emily Smith', '17-03-2020'),
        Order(6, 'Josie McGoth', '28-04-2021')
    ]

"""
Test create method. When calling create on an instance of OrderRpository, and passing through an instance of the order class, the order instance will be added to the database as a new row in table orders
"""

def test_create_method(db_connection):
    db_connection.seed("seeds/items_orders.sql")
    repository = OrderRepository(db_connection)
    new_order = Order(None, "Roy Miller", "03-06-2021")
    repository.create(new_order)
    assert repository.all() == [
        Order(1,'Ellie Priestley', '11-08-2023'),
        Order(2, 'Julian Vallender', '07-01-2023'),
        Order(3, 'Sarah Olivia', '09-06-2022'),
        Order(4, 'Finn Priestley', '09-09-2022'),
        Order(5, 'Emily Smith', '17-03-2020'),
        Order(6, 'Josie McGoth', '28-04-2021'),
        Order(7, "Roy Miller", "03-06-2021")
    ]