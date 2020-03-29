from ackley import ackley
from griewank import griewank
from rastrigin import rastrigin
from rosenbrock import rosenbrock
from schwefel import schwefel
from sphere import sphere
from tsp import tsp
import pandas as pd



def run(function, param = None):
    shift = pd.read_csv('shift_data.csv')
    bias = pd.read_csv('bias.csv')
    if function == 'djibouti':
        res = tsp.solve_tsp('http://www.math.uwaterloo.ca/tsp/world/dj38.tsp')
    elif function == 'qatar':
        res = tsp.solve_tsp('http://www.math.uwaterloo.ca/tsp/world/qa194.tsp')
    elif function == 'griewank':
        res = griewank.minimize_griewank(param, shift, bias)
    elif function =='sphere':
        res = sphere.minimize_sphere(param, shift, bias)
    elif function == 'rastrigin':
        res = rastrigin.minimize_rastrigin(param, shift, bias)
    elif function == 'ackley':
        res = ackley.minimize_ackley(param, shift, bias)
    elif function == 'rosenbrock':
        res = rosenbrock.minimize_rosenbrock(param, shift, bias)
    elif function == 'schwefel':
        res = schwefel.minimize_schwefel(param, shift, bias)
    return res


