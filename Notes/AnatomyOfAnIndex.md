# Use the Index, Luke: Preface and Chapter 1 Notes

## Anatomy of An Index

- SQL queries read like English sentences that explain requested data.

- There is no requirement to understand the inner workings of a database to write SQL statements, thus, many developers have years of SQL experience but they know nothing about the process that happens in the database when SQL statements are executed.

- The only thing developers need to know is how to index.

- A basic explanation of an index is that "an index makes the query fast".

- It is built using a *create index* statement.

- It requires its own disk space and holds a copy of indexed table data.

- Indexes are pure redundancy.

- Indexing does not change table data, it only creates a new data structure that refers to the table.

- Indexes undergo constant change, therefore, it only handles accumlutated updates with each next printing.

- Indexes cannot store data sequentially because an *insert* statement would need to move the following entries to make room for the new one. With large data sets, this would be very time consuming.

# Part 2 of notes

- To solve this problem, indexes establish a logical order that is independant from physical order in memory.

- The logical order is established through a doubly linked list.

- Doubly linked lists are lists where each node has links to two neighboring entries, essentially a chain.

- New nodes are inserted between two existing nodes and updating the links to refer to the new node. 

- Each node's two links refer to the node before and after it.