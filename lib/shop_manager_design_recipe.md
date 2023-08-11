1. Extract nouns from the user stories or specification

        As a shop manager
        So I can know which items I have in stock
        I want to keep a list of my shop items with their name and unit price.

        As a shop manager
        So I can know which items I have in stock
        I want to know which quantity (a number) I have for each item.

        As a shop manager
        So I can manage items
        I want to be able to create a new item.

        As a shop manager
        So I can know which orders were made
        I want to keep a list of orders with their customer name.

        As a shop manager
        So I can know which orders were made
        I want to assign each order to their corresponding item.

        As a shop manager
        So I can know which orders were made
        I want to know on which date an order was placed.

        As a shop manager
        So I can manage orders
        I want to be able to create a new order.


        Nouns: shop items, shop item unit price, shop item name, quantity of items, orders, customer name, order date.

        Verbs: create a new item, assign order to corresponding item, create new order.


2. Infer the Table Name and Columns
Put the different nouns in this table. Replace the example with your own nouns.

        Record	    Properties
        items	    unit price, name, quantity
        orders	    customer name, order date
        
        Name of the first table (always plural): items
        Column names: unit_price, name, quantity

        Name of the second table (always plural): orders
        Column names: customer_name, order_date

3. Decide the column types.
Here's a full documentation of PostgreSQL data types.


        Table: items
        id: SERIAL
        unit_price: FLOAT
        name: text
        quantity: int

        Table: orders
        id: SERIAL
        customer_name: text
        order_date: text


4. Design the Many-to-Many relationship
Make sure you can answer YES to these two questions:

        Can one item have many orders? (Yes)
        Can one order have many items? (Yes)


5. Design the Join Table
The join table usually contains two columns, which are two foreign keys, each one linking to a record in the two other tables.

The naming convention is table1_table2.


    Join table for tables: items and orders
    Join table name: items_orders
    Columns: item_id, order_id


4. Write the SQL.
file: items_orders.sql

        CREATE TABLE items (
            id SERIAL PRIMARY KEY,
            unit_price FLOAT,
            name text,
            quantity int
        );

        CREATE TABLE orders (
            id SERIAL PRIMARY KEY,
            customer_name text,
            order_date text
        );

        CREATE TABLE items_orders (
            item_id int,
            order_id int,
            constraint fk_item foreign key(item_id) references items(id) ON DELETE CASCADE,
            constraint fk_order foreign key(order_id) references orders(id) ON DELETE CASCADE,
            PRIMARY KEY (item_id, order_id)
        )


);
5. Create the tables.
psql -h 127.0.0.1 shop_manager < items_orders.sql
