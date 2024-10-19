
"""
Solutions to module 4
Review date:
"""

student = "Alexander Hedene"
reviewer = ""

import math as m
import random as r
import concurrent.futures as future
import time as t
import numpy
import functools


def pc():
    return t.perf_counter()

def sphere_volume(n, d):
    rad = 1
    # n is a list of set of coordinates
    # d is the number of dimensions of the sphere 
    n_sphere = 0
    create_point = lambda : numpy.array([r.uniform(-rad,rad) for _ in range(d)])
    norm = lambda vec : numpy.sqrt(functools.reduce(lambda x, y: x + y, map(lambda x: x**2, vec)))
    n_sphere = len(list(filter(lambda x : norm(x) < rad, [create_point() for _ in range(n)])))
    return n_sphere/n*(2*rad)**d

def hypersphere_exact(n,d):
    rad = 1
    return (m.pi**(d/2)/m.gamma(d/2+1)*rad**d)

def sphere_volume_parallel1(n,d,np):
    with future.ProcessPoolExecutor(max_workers=np) as executor:
        futures = [executor.submit(sphere_volume, n // np, d) for _ in range(np)]
        
        results = sum([f.result() for f in futures])
    return results/np

# parallel code - parallelize actual computations by splitting data
def sphere_volume_parallel2(n,d,np):
    with future.ProcessPoolExecutor(max_workers=np) as executor:
        futures = executor.map(sphere_volume, np*[n//np], np*[d]) 
        results = sum(list(futures))
    return results/np 

def main():
    # part 1 -- parallelization of a for loop among 10 processes 
    n = 1000000
    d = 11
    res_no_p = 0
    
    start_no_p_part1 = pc()
    for _ in range (10):
        res_no_p += sphere_volume(n,d)
    end_no_p_part1 = pc()
       
    start_p_part1 = pc()
    res_p1 = sphere_volume_parallel1(n*10,d,10)
    end_p_part1 = pc()

    start_p_part2 = pc()
    res_p2 = sphere_volume_parallel2(n*10,d,10)
    end_p_part2 = pc()
    
    print(f"No parallel computing: time = {end_no_p_part1 - start_no_p_part1}")
    print(f"Parallel computing 1: time = {end_p_part1 - start_p_part1}")
    print(f"Parallel computing 2: time = {end_p_part2 - start_p_part2}")
    print(f"Result with no p: {res_no_p/10},  result with p1: {res_p1}, result with p2: {res_p2}, actual volume: {hypersphere_exact(10*n,d)}")
    
if __name__ == '__main__':
	main()
