import torch

def create_tensor(method, shape, value=0.0):
    """
    Returns: list
    """
    if method == "zeros":
            tensor = torch.zeros(shape)
    elif method == "ones":
            tensor = torch.ones(shape)
    elif method == "full":
        if value is None:
                raise ValueError("fill_value is required when method='full'")
        tensor = torch.full(shape, value)
    else:
        raise ValueError(f"Unsupported method: {method}. Use 'zeros', 'ones', or 'full'.")
        
    return tensor.tolist()