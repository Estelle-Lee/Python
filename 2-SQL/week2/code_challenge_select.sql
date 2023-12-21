--- using tables from 2-SQL/data/initdb/northwind.sql

-- Select all values in the company_name column of the customers table 
-- that begin with the letters 'Q' through 'Z' (inclusive); 
-- sort values in descending order.
SELECT company_name FROM customers
WHERE company_name >= 'Q%'
ORDER BY company_name DESC;


-- Get first and last name of each employee 
-- with a title of "Sales Representative"; 
-- sort by last_name, and within the same last name, 
-- sort by first_name.
select first_name, last_name from employees
where title='Sales Representative'
order by last_name, first_name;

-- Get first_name and home_phone of each employee 
-- whose first_name begins with the capital letter 'A' 
-- and whose home_phone includes the number '4'. 
-- Order by employee_id.
select first_name, home_phone from employees
where first_name like 'A%' 
and home_phone like '%4%'
order by employee_id;