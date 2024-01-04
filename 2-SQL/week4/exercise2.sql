select * from moma_artists limit 50;

select jsonb_pretty(info) as formatted_info
from moma_artists limit 50;

select 
info -> 'display_name' as name,
info -> 'nationality' as nationality
from moma_artists
order by id
limit 50;

select 
info -> 'display_name' as name,
info -> 'nationality' as nationality
from moma_artists
where info ->> 'nationality'='American'
order by id
limit 50;

insert into moma_artists (info) values (
	json_object('{{display_name, Ablade Glover}, {nationality, Ghanaian}}')
);

select info from moma_artists
order by id desc limit 1;