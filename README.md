TSP
** The chosen algorithm and a justification of this choice**

--I opted for the 2-opt optimization algorithm as it is a specialized algorithm specifically designed for the traveling salesman problem, essentially taking a route that crosses over itself, and then reorganizing it so that it no longer crosses over itself. It has proven to be one of the most efficient algorithms for this problem as it is specifically designed for it.

** The parameters of the algorithm**

--The URL of the tsp input file and the number of iterations are the inputs for my function, although I have also created a euclidean distance lambda function to be used for the evaluation of distances.

--** The final results, both solution and fitness.**

-- Thesolutions can be found in the submitted CSV files, djibouti_tsp_solution.csv and qatar_tsp_solution.csv. The total euclidean distances are approx 6664 and 10191 respectively.
-- The solution for Djibouti is 0.12% away from the optimal solution, while the solution for Qatar is 8.2% away from the optimum.

--** The number of function evaluations**

--The euclidean distance function was called 703 times for djibouti, and 18000 times for Qatar.
--** The stopping criterion**

--The stopping criterion is no improvement from one iteration to the next

--** The computational time**

--The computational time for Djibouti is 0.3 seconds, while the computational time for Qatar is 1.6 seconds. This includes the downloading of the data, the reformatting, and the actual solving of the optimization problem. This algorithm has a O(n2) time complexity.

--** The convergence curve (fitness as a function of time)** 
