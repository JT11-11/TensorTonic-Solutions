import pandas as pd

def handle_missing(data, fill_value):
    """
    Returns: dict with 'null_counts' (dict) and 'cleaned_data' (dict)
    """
    result = {}
    df = pd.DataFrame(data)

    result["null_counts"] = df.isna().sum().to_dict()
    result["cleaned_data"] = df.fillna(fill_value).to_dict(orient = "list")

    return result