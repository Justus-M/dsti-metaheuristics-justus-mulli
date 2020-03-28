from ackley import ackley
from griewank import griewank
from rastrigin import rastrigin
from rosenbrock import rosenbrock
from schwefel import schwefel
from sphere import sphere
from tsp import tsp
import pandas as pd


shift = pd.read_csv('shift_data.csv')
bias = pd.read_csv('bias.csv')

djibouti_solution = tsp.solve_tsp('http://www.math.uwaterloo.ca/tsp/world/dj38.tsp')
qatar_solution = tsp.solve_tsp('http://www.math.uwaterloo.ca/tsp/world/qa194.tsp')

res = griewank.minimize_griewank(50, shift, bias)
res = sphere.minimize_sphere(50, shift, bias)
res = griewank.minimize_griewank(50, shift, bias)
rastrigin.minimize_rastrigin(50, shift, bias)git
ackley.minimize_ackley(50, shift, bias)
rosenbrock.minimize_rosenbrock(50, shift, bias)
schwefel.minimize_schwefel(50, shift, bias)


