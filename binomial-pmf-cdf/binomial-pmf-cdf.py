import math

def binomial_pmf_cdf(n: int, p: float, k: int) -> dict:
    """
    Returns a dictionary with pmf and cdf.
    """
    # Write code here
    answer = {}
    count_pmf = math.comb(n, k)
    pmf = count_pmf * (p**k) * ((1-p) ** (n-k))

    cdf = 0
    for i in range(k+1):
        tcount_pmf = math.comb(n, i)
        temp_pmf = tcount_pmf * (p**i) * ((1-p) ** (n-i))
        cdf += temp_pmf

    answer["pmf"] = float(pmf)
    answer["cdf"] = float(cdf)

    return answer