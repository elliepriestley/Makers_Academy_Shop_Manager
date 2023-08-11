from lib.order import Order

"""
Test constructs correctly with public properties
"""

def test_constructs():
    order1 = Order(1, "Ellie Priestley", "17-09-2022")
    assert order1.id == 1
    assert order1.customer_name == "Ellie Priestley"
    assert order1.order_date == "17-09-2022"


"""
Test that two instances of the order class, which have the same properties, are recognised as  equal
"""

def test_equality():
    order1 = Order(1, "Ellie Priestley", "17-09-2022")
    order2 = Order(1, "Ellie Priestley", "17-09-2022")
    assert order1 == order2



"""
Test order class formats nicely
"""

def test_returns_formatted_version():
    order1 = Order(1, "Ellie Priestley", "17-09-2022")
    assert str(order1) == "Order(1, Ellie Priestley, 17-09-2022)"