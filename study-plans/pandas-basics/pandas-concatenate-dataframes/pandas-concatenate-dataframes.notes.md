- help to concat lines in a dataframe.
- you need to convert the data into dataframe first and put it in a list. U can use list comprehensions like`[pd.DataFrame(d) for d in dfs]`

- ignore_index removes the original index of the old dataframes and update it with the lastest index of the new lists.