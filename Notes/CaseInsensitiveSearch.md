# Case-Insensitive Search Using UPPER or LOWER

- You can ignore cases in a where clause by converting both sides of the comparison to an all caps notation using UPPER().

- However, UPPER() prevents index usage, causing possible performance issues.

- Function-Based indexes (FBI) solves this problem in databases where they're supported.

- SQL Server & MySQL require generated columns instead of FBIs.

- Statistics updages are important for accurate optimizer decisions.

- Always check execution plans when using case-insensitive searches.