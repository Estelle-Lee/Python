---use student, department, professor tables: prebuilded

select*from departments;
select*from students;
select*from professors;

select s.last_name from students s
union
select p.last_name from professors p;

--- find duplicates? union all: print everything
select s.last_name from students s
union all
select p.last_name from professors p;

select s.last_name from students s
union all
select p.last_name from professors p
order by last_name;

--- there are 11 students but this sql will print only 8 students
--- because inner join is filtering out 
---any students who have not declared a major and 
---thus have a null placeholder 
---in the major department id column 
select s.first_name, s.last_name, d.name
from departments d
inner join students s
on d.id=s.major_department_id;

--- will result 11 students - result correct
select s.first_name, s.last_name, d.name
from departments d
right join students s
on d.id=s.major_department_id;

--- will result 12 students, adding only major
select s.first_name, s.last_name, d.name
from departments d
full join students s
on d.id=s.major_department_id;

--- find no student department
select name from departments d
except
select distinct name from departments d
inner join students s
on s.major_department_id=d.id;