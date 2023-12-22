-- Select each company_name that 
-- begins with the letter 'D', 
-- including those of customers, shippers, 
-- and suppliers. Tip: Use the WITH keyword.
select * from customers;
--- company_name
select * from shippers;
--- company_name
select*from suppliers;
--- company_name

with names as (
	select company_name from customers
	union all
	select company_name from suppliers
	union all
	select company_name from shippers
)
select company_name from names
where company_name like 'D%';




-- Get the product_name of products that 
-- belong to categories having a category_name 
-- beginning with the letter 'C'. 
-- Use a subquery instead of a JOIN.
select * from products;
--- product_name, category_id
select * from categories;
--- category_id, category_name

select product_name from products p
join categories c
on p.category_id=c.category_id
where c.category_name like 'C%';
---result count 25

select product_name from products p
where exists (
	select*from categories c
	where c.category_id=p.category_id
	and c.category_name like 'C%'
);
---result count 25