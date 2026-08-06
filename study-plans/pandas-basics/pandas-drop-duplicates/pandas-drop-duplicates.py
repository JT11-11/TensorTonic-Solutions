import pandas as pd

def drop_duplicates(data):
    """
    Returns: list [rows_before, rows_after, cleaned_data]
    """
    df = pd.DataFrame(data)
    result = []
    result.append(df.shape[0])
    duplicate_no = df.duplicated().sum()
    result.append(df.shape[0] - duplicate_no)
    df.drop_duplicates(inplace = True)
    result.append(df.to_dict(orient = "list"))
    return result