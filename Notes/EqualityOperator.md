# The Equals Operator

> *"The equality operator is both the most trivial and the most frequently used SQL operator. Indexing mistakes that affect performance are still very common and where clauses that combine multiple conditions are particularly vulnerable."*

## Primary Keys

- Databases automatically create indexes for the primary key.

- Where clauses cannot match multiple rows due to the intrinsic uniqueness of primary keys.

- This makes selecting primary keys very quick since they're indexed and unique.

- However, fetching the quieried data after finding the correct primary key can bottleneck speed.

- But, using the INDEX UNIQUE SCAN (MySQL const), the operation can't deliver more than one entry so it doesn't access the table multiple times. Therefore, the bottleneck doesn't happen with INDEX UNIQUE SCAN.

## Concatenated Keys

- Concatenated indexes are composite indexes that span multiple columns.

- Order of columns in a concatenated index very much so affects speed and usability.

- The first column in a concatenated index is the primary sorting column. The second is for ties and so on.

- If concatenated indexes aren't used, and instead full table scans, performance issues can arise.

- An analogy of this is like searching for a last name and then first name in a phone directory, searching for a last name only is time consuming and difficult.

- Concatenated index queries can be reversed to improve query performance.

- Instead of creating multiple indexes, making a good concatenated index is faster.

- Less indexes when possible is better.

## Slow Indexes, Part II

- Changing an index affects all queries on an indexed table.

- Databases select indexes based on optimization criteria.

- If multiple access paths exist, the query optimizer is used to select the best one.

- Indexed queries can be slower than full table scans if certain criterion are present.

- For example, wide index ranges are used, many rows must be fetched individually, or poor filtering.

- Query optimizers rely on database statistics for execution plans.

- If no statistics are present, the optimizer uses default values.

- Default values can poorly guess the number of rows.

- INDEX RANGE SCAN can be slow if too many rows are fetched.

- Always check execution plans before changing indexes.