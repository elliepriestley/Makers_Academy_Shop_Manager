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
Test order """