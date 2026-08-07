import pandas as pd

def groupby_basics(data, group_col, value_col):
    """
    Returns: dict with 'sum', 'mean', 'count' (each a dict)
    """
    result = {}
    df = pd.DataFrame(data)

    result["sum"] = df.groupby(group_col)[value_col].sum().to_dict()
    result["mean"] = df.groupby(group_col)[value_col].mean().to_dict()
    result["count"] = df.groupby(group_col)[value_col].count().to_dict()

    return result