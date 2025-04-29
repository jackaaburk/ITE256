# Use the Index, Django: Documentation

## Discussion of the two indexes that Django added, and the queries that use them.



## Comparison of the query plans generated when one uses/doesn't use __iexact.



## Results of the runtime investigation, formatted into a table.

![RunTimeTable](./Images/RunTimeTable.png)

> Run times for iexact vs. exact. We can see that iexact run times increase significantly over large datasets, whereas exact run times are rather inconsiderable.

## Short summary of the takeaways of this activity. Specifically, additional warnings to Django developers who are considering using the __iexact feature in their ORM code.

