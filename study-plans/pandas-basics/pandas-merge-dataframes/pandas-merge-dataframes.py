import pandas as pd

def merge_dataframes(left, right, on, how):
    """
    Returns: dict of column to value lists
    """
    left_df = pd.DataFrame(left)
    right_df = pd.DataFrame(right)
    result = pd.merge(left_df,right_df, on = on, how = how)
    return result.to_dict(orient = "list")