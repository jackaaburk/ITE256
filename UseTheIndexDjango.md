# Use the Index, Django: Documentation

## Discussion of the two indexes that Django added, and the queries that use them.



## Comparison of the query plans generated when one uses/doesn't use __iexact.

> Without __iexact

- When one doesn't use __iexact, Django is able to use the index since it isn't case insensitve.

> With __iexact

- When one does use __iexact, Django is inable to use an index, possibly making it much slower.

Intuitively, index and index only scans are very heavily lengthened when using __iexact, since it instead turns into a sequential scan/bitmap, requiring the scan to go through more of the actual table/data instead of the index.

## Results of the runtime investigation, formatted into a table.

![RunTimeTable](./Images/RunTimeTable.png)

> Run times for iexact vs. exact. We can see that iexact run times increase significantly over large datasets, whereas exact run times are rather inconsiderable.

## Short summary of the takeaways of this activity. Specifically, additional warnings to Django developers who are considering using the __iexact feature in their ORM code.

