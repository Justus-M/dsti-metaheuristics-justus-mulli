import pandas as pd
import numpy as np
from scipy.optimize import minimize
import time
import matplotlib.pyplot as plt

def rosenbrock(x):
    z = x-shift[:len(x)].values+1
    value = sum((((z[:-1]**2)-z[1:])**2)*100+(z[:-1]-1)**2)+bias
    converge.append(value)
    return value

def minimize_rosenbrock(dim, shifts, biases):
    start = time.time()
    global shift, bias, converge
    shift = shifts['rosenbrock']
    bias = biases['rosenbrock'].values[0]
    converge = []
    x = np.zeros(dim)
    result = minimize(rosenbrock, x, method = 'Powell', options={'xtol':0.0001})
    print(f'done in {time.time() - start} seconds.')
    rosenbrock(result['x'])
    plt.plot(converge)
    plt.xlabel('# of evaluations')
    plt.ylabel('value')
    plt.title(f'Rosenbrock convergence plot - dim {dim}')
    return result
