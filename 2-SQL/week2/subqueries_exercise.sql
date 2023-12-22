-- problem: 
-- how can we find duplicate last names, 
-- in the combined list of last names 
-- from both the professors and students table?

-- approach: 
-- we must get the count of each last name, 
-- then we will know that any last name 
-- with a count>1 is a duplicate

select last_name from professors
union all
select last_name from students;

-->

with all_names as (
	select last_name from professors
	union all
	select last_name from students
)

-->

with all_names as (
	select last_name from professors
	union all
	select last_name from students
)
select last_name, count(*)
from all_names
group by last_name;

-->

with all_names as (
	select last_name from professors
	union all
	select last_name from students
)
select last_name, count(*)
from all_names
group by last_name
having count(*)>1;

----------------------------

select first_name, last_name, department_id from professors
union all
select first_name, last_name, major_department_id from students;

-->

select 'professor' as occupation, first_name, last_name, department_id from professors
union all
select 'student' as occupation, first_name, last_name, major_department_id from students;


-->


with people as (
	select 'professor' as occupation, first_name, last_name, department_id from professors
	union all
	select 'student' as occupation, first_name, last_name, major_department_id from students
)
select occupation, first_name, last_name, d.code
from people
join departments d
on department_id=d.id;

--> if you want to add null values

with people as (
	select 'professor' as occupation, first_name, last_name, department_id from professors
	union all
	select 'student' as occupation, first_name, last_name, major_department_id from students
)
select occupation, first_name, last_name, d.code
from people
left join departments d
on department_id=d.id;