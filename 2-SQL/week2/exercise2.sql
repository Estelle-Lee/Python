create table cars(
    id serial primary key,
    year int,
    make text not null,
    model text not null
);

insert into cars (year, make, model)
values (2020,'Toyato','Prius');

insert into cars (year, make, model)
values (2012,'Ford','Focus');

ALTER TABLE cars
ADD wheel_count INT NOT NULL DEFAULT 4;

insert into cars (year, make, model)
values (2020,'Nissan','Altima');

insert into cars (make, model, wheel_count)
values ('Elio','P5',3);

DELETE FROM cars
WHERE year IS null;

insert into divisions (name)
values ('Atlantic'),('Metropolitan'),('Pacific'),('Central');

insert into teams (city,name,home_colour,away_colour,division_id)
values ('New York', 'Islanders','Royal blue','White',2),
('Seattle','Kraken','Deep sea blue','White',3);

update divisions
set name='Cosmopolitan'
where name='Metropolitan';

delete from divisions
where name='Cosmopolitan';