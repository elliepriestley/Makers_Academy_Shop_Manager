from lib.item import Item
"""
Test item class constructs with public properties as expected
"""

def test_constructs():
    item1 = Item(1, 2.99, "Item Name", 7)
    assert item1.id == 1
    assert item1.unit_price == 2.99
    assert item1.name == "Item Name"
    assert item1.quantity == 7

"""
Test that two instances of item class, with the same properties, will be seen as equal
"""

def test_equality():
    item1 = Item(1, 2.99, "Item Name", 7)
    item2 = Item(1, 2.99, "Item Name", 7)
    assert item1 == item2

"""
Test that Item class formats the inputs nicely
"""

def test_formats():
    item1 = Item(1, 2.99, "Item Name", 7)
    assert str(item1) == "Item(1, 2.99, Item Name, 7)"