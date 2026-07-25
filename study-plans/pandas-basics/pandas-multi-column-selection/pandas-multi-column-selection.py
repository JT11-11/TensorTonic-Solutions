import pandas as pd

def select_columns(data, columns):
    """
    Returns: dict mapping selected column names to value lists
    """
    df = pd.DataFrame(data)
    result = {}
    selected_columns = df.loc[:,columns].to_dict(orient = "list")
    return selected_columns