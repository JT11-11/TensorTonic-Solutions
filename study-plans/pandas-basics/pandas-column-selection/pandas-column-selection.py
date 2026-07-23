import pandas as pd

def select_column(data, column):
    """
    Returns: dict with 'values' (list) and 'length' (int)
    """
    df = pd.DataFrame(data)
    result = {}

    result["values"] = df[column].tolist()
    result["length"] = df[column].count()

    return result