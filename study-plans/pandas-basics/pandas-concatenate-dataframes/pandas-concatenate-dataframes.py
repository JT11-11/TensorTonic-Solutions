import pandas as pd

def concat_dataframes(dfs):
    """
    Returns: list [shape, data] where shape is [rows, cols]
    """
    result = pd.concat([pd.DataFrame(d) for d in dfs], ignore_index=True)    
    
    return [list(result.shape), result.to_dict(orient="list")]