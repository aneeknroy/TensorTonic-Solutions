import numpy as np

def euclidean_distance(x: list, y: list) -> float:
    """
    Returns the Euclidean distance as a float.
    """
    fin = 0.0
    for j in range(len(x)):
        difference = np.square(x[j] - y[j])
        print(difference)
        fin += difference
            
    return float(np.sqrt(fin))
    
        