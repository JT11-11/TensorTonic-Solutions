Nothing much as most of the theory has been taught in the previous exercises. 



However, some things to note: 

1. if you want to count no fo types in a dataframe, you can do .dtypes.values_counts() but then it will return  pandas dtypes and not strings so before .value_counts(), you need to have to have a .astype(str)
2. to count no of columns do df.shape[1], replace 1 with 0 for rows.



df.shapes return a tuple: 

```
(number_of_rows, number_of_columns)
```