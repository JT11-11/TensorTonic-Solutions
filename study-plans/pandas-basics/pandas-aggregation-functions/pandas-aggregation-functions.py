import pandas as pd

def multi_agg(data, group_col, value_col, funcs):
    """
    Returns: dict mapping function name to {group: value} dict
    """
    result = {}
    df = pd.DataFrame(data)

    converted = df.groupby(group_col)[value_col]
    for function in funcs:
        result[function] = converted.agg(function).to_dict()

    return result