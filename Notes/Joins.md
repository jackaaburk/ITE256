# Join Notes

## Joining

- Joining transforms data from a normalized model into a denormalized model that can be used for different purposes.

- Joining only processes two tables at a time.

- The optimizer will evaluate every different join order and use the best one.

- Join order doesn't impact the result, but it can impact processing speed.

## Nested Loop Joins

- Nested loop joins use two queries, one to fetch the results and one from the driving query to fetch data from the other table.

- Indexing for nested loops is a function based index.

- A SQL join processes quicker than nested selectsas it avoids network communication.

- The number of database round trips is more significant for the response time than the amount of data transferred.

- ORM tools are used in different ways to change join behavior.

- Eager fetching is the ability to load subclause data and related objects.

- Nested loops are good if the driving query returns small amounts of data.