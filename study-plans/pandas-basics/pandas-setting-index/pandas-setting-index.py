import pandas as pd

def set_index_column(data, index_col):
    """
    Returns: dict with 'index_values', 'columns', 'data'
    """
    result = {}
    df = pd.DataFrame(data)
    df = df.set_index(index_col)

    result["index_values"] = df.index.tolist()
    result["columns"] = df.columns.tolist()
    result["data"] = df.to_dict(orient = "list")

    return result