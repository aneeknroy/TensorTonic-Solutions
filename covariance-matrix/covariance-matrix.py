import numpy as np

def covariance_matrix(X: list) -> np.ndarray:
    """
    Returns the covariance matrix as a NumPy array.
    """
    # Write code here

    X = np.array(X)

    # Center the features
    X_centered = X - np.mean(X, axis=0)

    # find cross product
    cross = np.matmul(X_centered.T, X_centered)
    cov_matrix = np.divide(cross, (len(X) - 1))

    return cov_matrix
    
        