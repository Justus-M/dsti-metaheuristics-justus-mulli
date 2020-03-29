# DSTI Metaheuristics Assignment Justus Mulli

# Requirements:
* tspy, scipy, pandas, numpy and matplotlib
* simply type "pip install [package_name]" for each of the above packages into your terminal

To run these functions, simply clone the directory, and then set the directory to the main folder of this repository. then simply import optimization, and call 'optimization.run(function, param)'.

To run the traveling salesman optimization, simply type in 'djibouti' or 'qatar' in place of function, and ignore param. To run the optimization of one of the 6 optimization test functions, write the objective function name (either 'griewank', 'sphere', 'rastrigin', 'rosenbrock', 'schwefel', or 'ackley') and include param = dim, with dim being the dimension of the vector to optimize. Ex. optimization.run('sphere', param = 50) or optimization.run('rosenbrock', param = 500)

