import numpy as np

def expected_value_discrete(x: list, p: list) -> float:
    """
    Returns the expected value as a Python float.
    """
    # Write code here

    expectedValue = 0
    x = np.array(x, dtype=float)
    p = np.array(p, dtype=float)

    for var in range(len(x)):
        temp = x[var] * p[var]
        expectedValue += temp

    return expectedValue