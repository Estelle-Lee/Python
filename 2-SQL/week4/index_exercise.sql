-- postgres has a built in table named pg_indexes
-- that stores some metadata about the indexes,
-- such as a tablename and indexname.
select * from pg_indexes;

-- default indexes both use the b-tree data structure
-- which is more flexible than the hash index
-- which can only be leveraged when checking for equality
select tablename, indexname, indexdef from pg_indexes
where tablename not like 'pg_%';


--benchmark result: best 93 msec. 874 rows affected.
select title from moma_works
where artist='Frank Lloyd Wright';

-- b-tree index on the artist column
create index moma_works_btree_index
on moma_works(artist);

-- confirm in the pg_indexes table
select tablename, indexname, indexdef
from pg_indexes
where tablename not like 'pg_%';

--benchmark result: best 67 msec. 874 rows affected.
select title from moma_works
where artist='Frank Lloyd Wright';

--replace the b-tree index with a hash index
drop index moma_works_btree_index;

create index moma_works_hash_index 
on moma_works using HASH (artist);

-- confirm in the pg_indexes table
select tablename, indexname, indexdef
from pg_indexes
where tablename not like 'pg_%';

--benchmark result: best 58 msec. 874 rows affected.
select title from moma_works
where artist='Frank Lloyd Wright';

-- CHECK
drop index moma_works_hash_index;