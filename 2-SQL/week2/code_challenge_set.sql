--- from northwinid

---For each product, list the product_name 
---and the corresponding category_name.


-- For each order, list the order_id 
-- and the corresponding shipper company_name 
-- if available, else NULL.


-- For each customer order, 
-- list the customer's company_name, order_id, 
-- and total quantity of products ordered.

select*from products;
---product_name, category_id

select*from categories;
---category_id, category_name

select p.product_name, c.category_name
from products p
left join categories c
on p.category_id=c.category_id;
---result 77

SELECT product_name, category_name 
FROM products p 
JOIN categories c 
ON p.category_id = c.category_id;
---result 77

select*from orders;
---order_id, ship_name
select*from shippers;
---company_name: 6

select order_id, ship_name as company_name
from orders o
left join shippers s
on o.ship_name=s.company_name;

select*from customers;
---company_name
select*from orders;
---order_id, 
select*from order_details;
---order_id, quantity

select c.company_name, o.order_id, sum(od.quantity)
from orders o
join order_details od
on o.order_id=od.order_id
join customers c
on o.customer_id=c.customer_id
group by o.order_id, c.company_name;
inner join orders o
on c.company_name=o.company_name
