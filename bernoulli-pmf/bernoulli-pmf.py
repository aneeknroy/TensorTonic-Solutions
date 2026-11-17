import numpy as np

def bernoulli_pmf_and_moments(x: list, p: float) -> dict:
    """
    Returns a dictionary with pmf, mean, and variance.
    """
    # Write code here
    answer = {}
    pmf = []
    for j in x:
        if j == 0:
            pmf.append(1-p)
        else:
            pmf.append(p)

    answer["pmf"] = np.array(pmf, dtype = float)
    answer["mean"] = float(p)
    answer["variance"] = float(p*(1-p))

    return answer