import numpy as np

def dot_product(x: list, y: list) -> float:
    """
    Returns the dot product as a float.
    """
    fin = 0
    for j in range(len(x)):
        fin += x[j] * y[j]

    return float(fin)