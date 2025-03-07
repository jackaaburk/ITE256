# Query Plans

## Sequential Scan

1. the query

> EXPLAIN SELECT date_of_birth FROM employees;

2. the query plan

>                             QUERY PLAN

> ------------------------------------------------------------------

>  Seq Scan on employees  (cost=0.00..15286.00 rows=100000 width=4)

> (1 row)


3. A short explanation of why it used the operation it did

> Sequential scans are most efficient when most rows need to be scanned, since here it retrieves every date_of_birth entry from the entire table, sequential scan is used.

## Index Scan

1. the query

> EXPLAIN SELECT date_of_birth FROM employees WHERE (employee_id = 2);

2. the query plan

>                                  QUERY PLAN

> ------------------------------------------------------------------------------

>  Index Scan using employees_pk on employees  (cost=0.29..8.31 rows=1 width=4)

>    Index Cond: (employee_id = '2'::numeric)

> (2 rows)

3. A short explanation of why it used the operation it did

> Index scans use the index but still need to access the table to get additional data. Since here the SELECT statement is searching for employee_id = 2, it needs to access the table to find the specific employee_id row. Thus, an index scan is used.

## Index Only Scan

1. the query

> EXPLAIN SELECT COUNT(*) FROM employees;

2. the query plan

>                                            QUERY PLAN

> -------------------------------------------------------------------------------------------------

> Aggregate  (cost=2859.29..2859.30 rows=1 width=8)

>    ->  Index Only Scan using employees_pk on employees  (cost=0.29..2609.29 rows=100000 width=0)

> (2 rows)

3. A short explanation of why it used the operation it did

> Index only scans are where the query only needs to use the primary key from the table, in this case that is true because we are just counting entries. Thus, it used a index only scan
