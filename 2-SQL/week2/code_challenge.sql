create table divisions(
	id serial primary key,
	name text not null unique
);
create table teams(
	id serial primary key,
	city text not null,
	name text not null unique,
	home_colour text not null,
	away_colour text,
	division_id int
);

alter table teams
add constraint fk_teams_divisions
foreign key(division_id)
references divisions
on delete set null;

