import numpy as np

def sample_var_std(x: list) -> dict:
    """
    Returns a dictionary with variance and standard_deviation.
    """
    # Write code here
    answer = {}
    sum = 0
    avg = np.average(x)
    for j in x:
        temp = (j - avg) ** 2
        sum += temp

    sv = sum / (len(x) - 1)
    sd = np.sqrt(sv)

    answer["variance"] = float(sv)
    answer["standard_deviation"] = float(sd)

    return answer