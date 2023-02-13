

The <code>sales</code> database is simplified kernel of a database that any company might have that fulfills orders, whether that be online or in bricks-and-mortar stores.  The database has three tables:

- <code>item</code>
- <code>order</code>
- <code>order_item</code>

The <code>item</code> table documents data relating to each of the best-selling books and movies that the company sells.  The <code>order</code> table contains ID codes for each order and the date on which the order was placed.  Each row/record in the <code>order_item</code> table documents item IDs associated with order and the quantity of each item that was ordered.  The database is shown visually below in an Entity-Relationship (ER) Diagram.  Note the foreign key relationships between the <code>order_item</code> table and the other two tables.


![alt text](.guides/img/jb/er.jpg)