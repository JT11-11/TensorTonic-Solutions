- this exercise allows us to fill the missing values easily.
- you can use .isna() and then it will return the places where values are True/False of if the values are NaN.
- .isna().sum() allows u to sum total na values per column
- .fillna(fill_value) allows u to fill each of the data with a value . 

- if u add in an additional argument of inplace = True, then u return None as it will actively change the df itself without returning anything.