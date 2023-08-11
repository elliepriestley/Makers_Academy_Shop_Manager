from lib.item_repository import ItemRepository
from lib.database_connection import DatabaseConnection
from lib.item import Item

"""
Test all method returns a list of all items from the database
"""

def test_all_method_returns_all_items(db_connection):
    db_connection.seed("seeds/items_orders.sql")
    repository = ItemRepository(db_connection)
    result = repository.all()
    assert result == [
        Item(1, 150.99, 'Mechanical Keyboard', 10 ),
        Item(2, 429.99, 'Playstation 5', 5),
        Item(3, 299.00, 'Samsung Monitor', 33),
        Item(4, 170.50, 'Acer Laptop', 14 ),
        Item(5, 15.99, 'Mobile Phone Screen Protector', 50 ),
        Item(6, 70.00, 'Keycap Switch Pack', 67),
        Item(7, 119.9, 'Kindle Paperwhite', 48),
        Item(8, 350.00, 'Apple IPad', 5 ),
        Item(9, 15.99, 'Laptop Case', 57),
        Item(10, 1799.00, 'Macbook Pro', 10),
        Item(11, 30.50, 'Wired Headphones', 22)
    ]

"""
Test create method. When we call create method on ItemRepository instance, passing through an instance of the item class, this item is added as a new row to the items table in the database
"""

def test_create_method(db_connection):
    db_connection.seed("seeds/items_orders.sql")
    repository = ItemRepository(db_connection)
    item1 = Item(None, 2.99, "Pack of Pens", 30)
    repository.create(item1)
    assert repository.all() == [
        Item(1, 150.99, 'Mechanical Keyboard', 10 ),
        Item(2, 429.99, 'Playstation 5', 5),
        Item(3, 299.00, 'Samsung Monitor', 33),
        Item(4, 170.50, 'Acer Laptop', 14 ),
        Item(5, 15.99, 'Mobile Phone Screen Protector', 50 ),
        Item(6, 70.00, 'Keycap Switch Pack', 67),
        Item(7, 119.9, 'Kindle Paperwhite', 48),
        Item(8, 350.00, 'Apple IPad', 5 ),
        Item(9, 15.99, 'Laptop Case', 57),
        Item(10, 1799.00, 'Macbook Pro', 10),
        Item(11, 30.50, 'Wired Headphones', 22),
        Item(12, 2.99, "Pack of Pens", 30)
    ]

"""
Test find_by_order method. When calling the find_by_order method and passing through an order id, a list will be returned containing all items on that particular order. 
"""

# def test_find_by_order_method(db_connection):
#     db_connection.seed("seeds/items_orders.sql")
#     repository = ItemRepository(db_connection)
#     assert repository.find_by_order(1) == [
#         Item(1, 150.99, 'Mechanical Keyboard', 10),
#         Item(6, 70, 'Keycap Switch Pack', 67),
#         Item(9, 15.99, 'Laptop Case', 57)
#     ]
