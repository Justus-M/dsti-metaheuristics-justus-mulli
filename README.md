# DSTI Metaheuristics Assignment Justus Mulli

Requirements: tspy, scipy, pandas, numpy and matplotlib
simply type "pip install [package_name]" for each of the above packages into your terminal

To run these functions, simply clone the directory, and then set the directory to the main folder of this repository. then simply import optimization, and call 'optimization.run(function, param)'.

To run the traveling salesman optimization, simply type in 'djibouti' or 'qatar' in place of function, and ignore param. To run the optimization of one of the 6 optimization test functions, write the objective function name (either 'griewank', 'sphere', 'rastrigin', 'rosenbrock', 'schwefel', or 'ackley') and include param = dim, with dim being the dimension of the vector to optimize. Ex. optimization.run('sphere', param = 50) or optimization.run('rosenbrock', param = 500)

## TSP

###### The chosen algorithm and a justification of this choice

I opted for the 2-opt optimization algorithm as it is a specialized algorithm specifically designed for the traveling salesman problem, essentially taking a route that crosses over itself, and then reorganizing it so that it no longer crosses over itself. It has proven to be one of the most efficient algorithms for this problem as it is specifically designed for it.

###### The parameters of the algorithm 

The URL of the tsp input file and the number of iterations are the inputs for my function, although I have also created a euclidean distance lambda function to be used for the evaluation of distances.

###### The final results, both solution and fitness.**

Thesolutions can be found in the submitted CSV files, djibouti_tsp_solution.csv and qatar_tsp_solution.csv. The total euclidean distances are approx 6664 and 10191 respectively.

The solution for Djibouti is 0.12% away from the optimal solution, while the solution for Qatar is 8.2% away from the optimum.

###### The number of function evaluations**

--The euclidean distance function was called 703 times for djibouti, and 18000 times for Qatar.
--** The stopping criterion**

--The stopping criterion is no improvement from one iteration to the next

--** The computational time**

--The computational time for Djibouti is 0.3 seconds, while the computational time for Qatar is 1.6 seconds. This includes the downloading of the data, the reformatting, and the actual solving of the optimization problem. This algorithm has a O(n2) time complexity.

--** The convergence curve (fitness as a function of time)** 
