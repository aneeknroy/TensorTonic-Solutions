import numpy as np

def manhattan_distance(x: list, y: list) -> float:
    """
    Returns the Manhattan distance as a Python float.
    """
    # Write code here
    fin = 0
    for num in range(len(x)):
        fin += abs(x[num] - y[num])

    return float(fin)