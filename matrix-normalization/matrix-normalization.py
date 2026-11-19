import numpy as np

def matrix_normalization(matrix: list, axis=None, norm_type: str = "l2") -> np.ndarray:
    """
    Returns a NumPy array with the same shape as matrix.
    """
    # Write code here
    matrix = np.array(matrix)
    fin = []
    if axis == None:
        if norm_type == "l1":
            return matrix / np.linalg.norm(matrix.ravel(), ord=1)
        if norm_type == "l2":
            return matrix / np.linalg.norm(matrix.ravel(), ord=2)
        if norm_type == "max":
            return matrix / np.linalg.norm(matrix.ravel(), ord=np.inf)
            
    match norm_type:
        case "l1":
            if axis == 0: # column        
                for column in matrix.T:
                    norm = np.linalg.norm(column, ord=1)
                    column = np.array(column / (norm if norm != 0 else 1))
                    fin.append(column)
            else:
                for row in matrix:
                    norm = np.linalg.norm(row, ord=1)
                    row = np.array(row / (norm if norm != 0 else 1))
                    fin.append(row)
        case "l2":
            if axis == 0: # column           
                for column in matrix.T:
                    norm = np.linalg.norm(column, ord=2)
                    column = np.array(column / (norm if norm != 0 else 1))
                    fin.append(column)
            else:
                for row in matrix:
                    norm = np.linalg.norm(row, ord=2)
                    row = np.array(row / (norm if norm != 0 else 1))
                    fin.append(row)
        case "max":
            if axis == 0: # column           
                for column in matrix.T:
                    norm = np.linalg.norm(column, ord=np.inf)
                    column = np.array(column / (norm if norm != 0 else 1))
                    fin.append(column)
            else:
                for row in matrix:
                    norm = np.linalg.norm(row, ord=np.inf)
                    row = np.array(row / (norm if norm != 0 else 1))
                    fin.append(row)

    fin = np.array(fin)
    
    if axis == 0:
        return fin.T
    else:
        return fin