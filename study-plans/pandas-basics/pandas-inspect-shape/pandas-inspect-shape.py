import pandas as pd

def inspect_dataframe(data):
    """
    Returns: dict with 'rows', 'cols' (ints), 'columns' (list),
    'dtypes' (dict), 'total_values' (int)
    """
    df = pd.DataFrame(data)
    
    result = {}
    result["rows"] = df.shape[0]
    result["cols"] = df.shape[1]
    result["columns"] = df.columns.tolist()
    result["dtypes"] = df.dtypes.astype(str).to_dict()
    result["total_values"] = df.size
    
    return result