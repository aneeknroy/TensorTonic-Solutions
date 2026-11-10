from collections import Counter
import numpy as np

def mean_median_mode(x: list) -> dict:
    """
    Returns a dictionary with mean, median, and mode.
    """
    # Write code here
    fin = {}
    fin["mean"] = float(np.mean(x))
    fin["median"] = float(np.median(x))
    vals, counts = np.unique(x, return_counts=True)
    fin["mode"] = float(vals[np.argmax(counts)])

    return fin