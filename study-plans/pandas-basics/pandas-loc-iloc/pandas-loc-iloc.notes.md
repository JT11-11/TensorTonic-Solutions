New chapter introducing loc and iloc.

- loc refers to the label based indexing. 

- it is inclusive when indexing like df.loc['row1', 'row2'] --&gt; row2 is inclusive
- u can also do conditionals like:

```
df.iloc[score&gt;30,2]
```

- iloc is indexing based on the row/column number

- it is exclusive when indexing like df.iloc[1:2] --&gt; exclusive of 2nd row
- ** zero based indexing --&gt; all index starts from 0**

- Assignments: 

- Assigning of variables to loc and iloc is via:

```
df.iloc[score&gt; 30, 2] = variable_name
```

- if u do `df[row][column]`, you will most likely change the copy of the dataframe instead of the inplace one.