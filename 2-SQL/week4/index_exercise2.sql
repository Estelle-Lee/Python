-- developer tools to help developers understand
-- what exactly is going on under the hood when a query is executed

-- explain: provide information about the query plan
explain select date_acquired from moma_works
where date_acquired between '1950-01-01' and '1959-12-31';

-- explain analyze: provide information about the query plan,
-- but also the cost of each step including planning and execution
explain analyze select date_acquired from moma_works
where date_acquired between '1950-01-01' and '1959-12-31';

-- improve query runtime by creating an index
-- since between keyword is an abstraction of >= and <=
-- so b-tree index is good candidate (default index)
create index date_acq_idx on moma_works(date_acquired);

explain analyze select date_acquired from moma_works
where date_acquired between '1950-01-01' and '1959-12-31';
