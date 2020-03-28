import pandas as pd
import numpy as np
from scipy.optimize import basinhopping
import time
import matplotlib.pyplot as plt


def ackley(x):
    l = len(x)
    z = x - shift[:l]
    val = -20*np.exp(-0.2*np.sqrt((1/l)*sum(z**2)))-np.exp((1/l)*sum(np.cos(2*np.pi*z)))+20+np.e+bias
    converge.append(val)
    return val

def minimize_ackley(dim, shifts, biases):
    start = time.time()
    global shift, bias, converge
    shift = shifts['ackley']
    bias = biases['ackley'].values[0]
    converge = []
    x = np.zeros(dim)
    minimizer_kwargs = {"method": "Powell"}
    result = basinhopping(ackley, x, minimizer_kwargs=minimizer_kwargs, niter=10)
    print(f'done in {time.time() - start} seconds.')
    plt.plot(converge)
    plt.xlabel('# of evaluations')
    plt.ylabel('value')
    plt.title(f'Ackley convergence plot - dim {dim}')
    return result

