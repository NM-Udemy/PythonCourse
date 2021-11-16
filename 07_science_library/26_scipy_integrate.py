from scipy.integrate import quad
import numpy as np

def f(x):
    return 2 * x + 3
print(quad(f, 1, 2))

print(quad(lambda x: np.sin(x), 0, np.pi))