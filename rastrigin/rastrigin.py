import pandas as pd
import numpy as np
from scipy.optimize import basinhopping
import time
import matplotlib.pyplot as plt

def rastrigin(x):
    z = x - shift[:len(x)]
    val = sum((z**2)-10*np.cos(2*np.pi*z)+10)+bias
    converge.append(val)
    return val

def minimize_rastrigin(dim, shifts, biases):
    start = time.time()
    global shift, bias, converge
    shift = shifts['rastrigin']
    bias = biases['rastrigin'].values[0]
    converge = []
    x = np.zeros(dim)
    minimizer_kwargs = {"method": "Powell"}
    result = basinhopping(rastrigin, x, minimizer_kwargs=minimizer_kwargs, niter = 10)
    print(f'done in {time.time() - start} seconds.')
    plt.plot(converge)
    plt.xlabel('# of evaluations')
    plt.ylabel('value')
    plt.title(f'Rastrigin convergence plot - dim {dim}')
    return result

