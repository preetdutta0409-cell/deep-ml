def matrixmul(a:list[list[int|float]],b:list[list[int|float]])-> list[list[int|float]]:
    import numpy as np
    try:
        # Try to multiply the matrices and convert the result to a list
        return (np.asarray(a) @ np.asarray(b)).tolist()
    except ValueError:
        # If dimensions mismatch, NumPy throws a ValueError; catch it and return -1
        return -1
