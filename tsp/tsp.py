import pandas as pd
import numpy as np
import tspy
from tspy.solvers import TwoOpt_solver
import time


def pandas_read_tsp(url):
    frame = pd.read_csv(url, error_bad_lines = False)
    data_marker = frame.set_index(frame.columns[0]).index.get_loc('NODE_COORD_SECTION') + 1
    frame = frame.loc[data_marker:]
    frame.columns = ['data']
    frame = pd.DataFrame(frame.data.str.split(' ',2).tolist())[[1,2]].dropna()
    frame[1], frame[2] = pd.to_numeric(frame[1]), pd.to_numeric(frame[2])
    return frame


def solve_tsp(tsp_url, iterations = 100):
    start = time.time()
    tsp = tspy.TSP()
    data = pandas_read_tsp(tsp_url)
    tsp.read_data(data.values, lambda a,b: np.sqrt(sum((a-b)**2)))
    two_opt = TwoOpt_solver(initial_tour='NN', iter_num=iterations)
    two_opt_tour = tsp.get_approx_solution(two_opt)
    print(f'done after {time.time()-start} seconds')
    tsp.plot_solution('TwoOpt_solver')
    return tsp.get_best_solution()


