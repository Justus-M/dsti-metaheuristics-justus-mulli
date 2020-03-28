import pandas as pd
import numpy as np
from scipy.optimize import minimize
import time
import matplotlib.pyplot as plt

def schwefel_array(x):
    shape = x.shape[0]
    if len(x.shape) == 2: shape = x.shape[1]
    value = np.max(np.abs(x-shift[0:shape].values.reshape(1, shape)), axis = 1) + bias
    return value

def schwefel(x):
    return max(np.abs(x-shift[0:len(x)].values)) + bias

def minimize_schwefel(dim, shifts, biases, array = False):
    step_size = 50
    reduced = 0
    start = time.time()
    global shift, bias, eval_count, converge
    shift = shifts['schwefel']
    bias = biases['schwefel'].values[0]
    converge = []
    x = np.zeros(dim)
    val = schwefel(x)
    best_val = val
    no_improvement = 0
    counter = 0
    id = np.identity(dim)
    t = np.append(id, id * -1).reshape(len(id) * 2,-1)*step_size
    while no_improvement == 0:
        temp = x+t
        if array:
            step = schwefel_array(temp)
        else:
            step = np.apply_along_axis(schwefel, 1, temp)
        converge.append(min(step))
        val = min(step)
        if val < best_val:
            best_val = val
            improved_index = np.argmin(step)
            x = temp[improved_index]
            counter += 1
            print(f'iteration {counter}')
            print(f'score{best_val}')
            continue
        if reduced <7:
            t/=2
            reduced+=1
            continue
        break
    print(f'done after {time.time()-start} seconds.')
    plt.plot(converge)
    plt.xlabel('# of Iterations')
    plt.ylabel('value')
    plt.title(f'Schwefel convergence plot - dim {dim}')
    return x

