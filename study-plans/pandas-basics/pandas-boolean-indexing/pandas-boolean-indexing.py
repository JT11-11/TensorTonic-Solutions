import pandas as pd

def boolean_filter(data, column, threshold):
    """
    Returns: dict with 'filtered_data' (dict) and 'count' (int)
    """
    df = pd.DataFrame(data)
    result = {}

    filter = df[column] > threshold
    result["filtered_data"] = df[filter].to_dict(orient = "list")
    result["count"] = len(df[filter])

    return result
    
    