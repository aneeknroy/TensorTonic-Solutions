import numpy as np

def vector_norms(v: list) -> np.ndarray:
    """
    Returns a float64 array containing the L1, L2, and infinity norms.
    """
    l1 = np.linalg.norm(v, ord=1)
    l2 = np.linalg.norm(v, ord=2)
    linf = np.linalg.norm(v, ord=np.inf)

    return np.array([l1, l2, linf], dtype=np.float64)