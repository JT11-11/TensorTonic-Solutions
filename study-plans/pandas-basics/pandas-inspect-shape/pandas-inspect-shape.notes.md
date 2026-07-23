1. if u do .shape, u can take the values with [] just like a normal list
2. if u wanna convert to list/dict, just use .tolist() and todict()
3. if u want the total size of the dataframe, do .size
4. there might be instances in the dtypes that it cannot be serialize into JSON like INT64 as JSON does not recognize this. Therefore, to solve this , we needc to use the astype() before the to_dict() so that it can be converted properly via converting indiv types to string format.