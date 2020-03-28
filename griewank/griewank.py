import pandas as pd
import numpy as np
from scipy.optimize import minimize
import time
import matplotlib.pyplot as plt

def griewank(x):
    z = x - shift[:len(x)]
    val = (sum(z**2)/4000)-np.cumprod(np.cos(z/np.sqrt(np.arange(len(z))+1))).values[-1]+1+bias
    converge.append(val)
    return val

def minimize_griewank(dim, shifts, biases):
    start = time.time()
    global shift, bias, converge
    shift = shifts['griewank']
    bias = biases['griewank'].values[0]
    converge = []
    x = np.zeros(dim)
    result = minimize(griewank, x, options={'gtol':0.1})
    print(f'done in {time.time() - start} seconds.')
    plt.plot(converge)
    plt.xlabel('# of evaluations')
    plt.ylabel('value')
    plt.title(f'Griewank convergence plot - dim {dim}')
    return result

