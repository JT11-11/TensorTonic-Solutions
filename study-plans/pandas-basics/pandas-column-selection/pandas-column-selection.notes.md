1. before every data manipulation, always do pd.DataFrame() to ensure that  you can convert the data to df form.
2. if u are taking a column(s), u can do it in 2 methods 

1. df[column] --&gt; this gives a 1-d column
2. df[[column,column]] --&gt; this gives a 2-d column and allows u to extract more than one column
3. if u wanna find a length of a dataframe, you can do: 

1. len(df['column')
2. df["column"].size
3. df["column"].count()
4. Note: u cannot do df[column] and return that as a list of values. You need to .tolist() after as df[column] returns a Pandas series which is smth like the following:

```
0    Alice
1      Bob
Name: name, dtype: object
```