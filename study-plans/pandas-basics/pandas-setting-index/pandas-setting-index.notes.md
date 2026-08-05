- Indexing a column can help faster lookup --&gt; will auto drop that col from the main df itself 

- do not create another dataframe if u do .set_index else the original dataframe will not get the column dropped.
- to extract index list, use .index
- If u wanna not drop, use "drop = False"