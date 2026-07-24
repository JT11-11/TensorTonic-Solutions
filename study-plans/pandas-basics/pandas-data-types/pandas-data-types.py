import pandas as pd

def data_types_overview(data):
    """
    Returns: dict with 'dtypes', 'type_counts', 'num_columns'
    """
    df = pd.DataFrame(data)
    result = {}

    result["dtypes"] = df.dtypes.astype(str).to_dict()
    result["type_counts"] = df.dtypes.astype(str).value_counts().to_dict()
    result["num_columns"] = df.shape[1]
    
    return result