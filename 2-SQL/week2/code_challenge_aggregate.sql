-- For each customer, 
-- list the customer_id and the order_date 
-- of their first order. Sort by customer_id.
select genre, count(*) as c from books
group by genre
having c>1;


-- For each customer, 
-- list customer ID and the average freight cost 
-- of their orders; sort by average freight cost.
select customer_id, AVG(freight) as AVG_freight from orders
group by customer_id
order by AVG_freight;


-- For each order, 
-- select the order_id and the number of distinct products 
-- in said order (call this product_count). 
-- Filter to only include orders 
-- with a product_count of 5 or more 
-- Sort by product_count in descending order.
select customer_id, AVG(freight) as AVG_freight from orders
group by customer_id
order by AVG_freight;