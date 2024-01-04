-- employee.drawio

create table employees(
	id SERIAL PRIMARY KEY,
	salary INTEGER NOT NULL,
	name TEXT NOT NULL
);

CREATE TABLE employees_log(
	id SERIAL PRIMARY KEY,
	description TEXT NOT NULL,
	created_at TIMESTAMP NOT NULL DEFAULT now(),
	employee_id INT NOT NULL,
	CONSTRAINT fk_emp_log_to_emp
	FOREIGN KEY (employee_id) REFERENCES employees(id)
	ON DELETE CASCADE
);

CREATE FUNCTION log_new_employee() RETURNS trigger AS $$
	BEGIN
		INSERT INTO employees_log (description, employee_id) VALUES (
			'Employee created.',
			NEW.id
		);
		RETURN NEW;
	END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER log_new_employee AFTER INSERT ON employees
	FOR EACH ROW EXECUTE FUNCTION log_new_employee();
	
INSERT INTO employees (salary, name) 
values (55000, 'Alice'),(66000,'Bob');

select e.*, el.description, el.created_at
from employees_log el
join employees e
on el.employee_id=e.id;

create function log_salary_update()
returns trigger as $$
	begin
		insert into employees_log (description, employee_id)
		values ('Salary updated from '||OLD.salary||' to '||NEW.salary,
			   NEW.id
		);
		return NEW;
	END;
$$ LANGUAGE plpgsql;

create trigger log_salary_update
after update of salary
on employees
	for each row
	execute function log_salary_update();
	
update employees
set salary=80000
where name='Alice';

select e.*, el.description, el.created_at
from employees_log el
join employees e on el.employee_id=e.id;

update employees set name='Alice B. Cool' where name='Alice';
	
select e.*, el.description, el.created_at
from employees_log el
join employees e on el.employee_id=e.id;

-- clean up
drop table employees CASCADE;
DROP TABLE employees_log;
drop function log_new_employee;
drop function log_salary_update;