CREATE TABLE orders(
    id serial primary key,
    amount_spent numeric not null,
    customer_id int not null,
    constraint fk_customer
        foreign key(customer_id)
        references customers(id)
        on delete cascade   ---forces delete all data when delete the foreign key.
);

--- set null, retains the value but to null 
-- create table orders (
--     id serial primary key,
--     amount_spent numeric not null,
--     customer_id int not null,
--     constraint fk_customer
--         foreign key(customer_id)
--         references customers(id)
--         on delete set null
-- );

--- set default, retains the value but to the default value
-- create table orders (
--     id serial primary key,
--     amount_spent numeric not null,
--     customer_id int not null,
--     constraint fk_customer
--         foreign key(customer_id)
--         references customers(id)
--         on delete set default
-- );


