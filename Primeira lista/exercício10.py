import numpy as np

def conversão(x, y):
    v1 = np.array([x, y])
    teta = np.arctan(y, x)
    r = np.linalg.norm(v1)
    return [r, teta]

