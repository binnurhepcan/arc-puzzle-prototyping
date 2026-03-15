import numpy as np

def solution(input_grid):
    arr = np.array(input_grid)
    mask = (arr > 0).astype(int)      
    op = np.kron(arr, mask)
    return op
