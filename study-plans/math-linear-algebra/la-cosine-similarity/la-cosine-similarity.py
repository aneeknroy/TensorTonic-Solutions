import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a float.
    """
    numerator = np.dot(a, b)
    denominator = np.linalg.norm(a, ord=2) * np.linalg.norm(b, ord=2)

    if denominator == 0:
        return float(0)
    
    return float(numerator/denominator)