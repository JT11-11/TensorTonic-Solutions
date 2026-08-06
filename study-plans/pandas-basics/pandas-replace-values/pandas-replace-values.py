import pandas as pd

def replace_values(data, column, old_val, new_val):
    """
    Returns: dict with 'data' (dict) and 'count' (int)
    """
    df = pd.DataFrame(data)
    result = {}
    count = df[column].eq(old_val).sum()
    df[column].replace(old_val, new_val, inplace = True)
    result["data"] = df.to_dict(orient = "list")
    result["count"] = count
    return result