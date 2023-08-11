ALTER TABLE items_orders
    DROP CONSTRAINT IF EXISTS
    fk_item;

ALTER TABLE items_orders
    DROP CONSTRAINT IF EXISTS
    fk_order;

DROP TABLE IF EXISTS items;
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS items_orders;


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
);

INSERT INTO items (unit_price, name, quantity) VALUES (150.99, 'Mechanical Keyboard', 10);
INSERT INTO items (unit_price, name, quantity) VALUES (429.99, 'Playstation 5', 5);
INSERT INTO items (unit_price, name, quantity) VALUES (299.00, 'Samsung Monitor', 33);
INSERT INTO items (unit_price, name, quantity) VALUES (170.50, 'Acer Laptop', 14);
INSERT INTO items (unit_price, name, quantity) VALUES (15.99, 'Mobile Phone Screen Protector', 50);
INSERT INTO items (unit_price, name, quantity) VALUES (70.00, 'Keycap Switch Pack', 67);
INSERT INTO items (unit_price, name, quantity) VALUES (119.9, 'Kindle Paperwhite', 48);
INSERT INTO items (unit_price, name, quantity) VALUES (350.00, 'Apple IPad', 5);
INSERT INTO items (unit_price, name, quantity) VALUES (15.99, 'Laptop Case', 57);
INSERT INTO items (unit_price, name, quantity) VALUES (1799.00, 'Macbook Pro', 10);
INSERT INTO items (unit_price, name, quantity) VALUES (30.50, 'Wired Headphones', 22);

INSERT INTO orders (customer_name, order_date) VALUES ('Ellie Priestley', '11-08-2023');
INSERT INTO orders (customer_name, order_date) VALUES ('Julian Vallender', '07-01-2023');
INSERT INTO orders (customer_name, order_date) VALUES ('Sarah Olivia', '09-06-2022');
INSERT INTO orders (customer_name, order_date) VALUES ('Finn Priestley', '09-09-2022');
INSERT INTO orders (customer_name, order_date) VALUES ('Emily Smith', '17-03-2020');
INSERT INTO orders (customer_name, order_date) VALUES ('Josie McGoth', '28-04-2021');

INSERT INTO items_orders (item_id, order_id) VALUES (1, 1);
INSERT INTO items_orders (item_id, order_id) VALUES (6, 1);
INSERT INTO items_orders (item_id, order_id) VALUES (9, 1);
INSERT INTO items_orders (item_id, order_id) VALUES (2, 2);
INSERT INTO items_orders (item_id, order_id) VALUES (11, 3);
INSERT INTO items_orders (item_id, order_id) VALUES (5, 3);
INSERT INTO items_orders (item_id, order_id) VALUES (3, 4);
INSERT INTO items_orders (item_id, order_id) VALUES (4, 5);
INSERT INTO items_orders (item_id, order_id) VALUES (9, 5);
INSERT INTO items_orders (item_id, order_id) VALUES (1, 6);
INSERT INTO items_orders (item_id, order_id) VALUES (5, 6);