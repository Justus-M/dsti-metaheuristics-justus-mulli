import pandas as pd
import numpy as np
from scipy.optimize import minimize
import time
import matplotlib.pyplot as plt

def sphere_evaluate(x):
    value = sum((x-shift[0:len(x)])**2)+bias
    converge.append(value)
    return value


def minimize_sphere(dim, shifts, biases):
    start = time.time()
    global shift, bias, converge
    shift = shifts['sphere']
    bias = biases['sphere'].values[0]
    converge = []
    x = np.zeros(dim)
    result = minimize(sphere_evaluate, x)
    print(f'done in {time.time()-start} seconds.')
    sphere_evaluate(result['x'])
    plt.plot(converge)
    plt.xlabel('# of evaluations')
    plt.ylabel('value')
    plt.title(f'Sphere convergence plot - dim {dim}')
    return result




