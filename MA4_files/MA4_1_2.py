
"""
Solutions to module 4
Review date:
"""

student = "Alexander Hedene"
reviewer = ""

import math as m
import random as r
import numpy as np
import functools

def sphere_volume(n, d):
    rad = 1
    # n is a list of set of coordinates
    # d is the number of dimensions of the sphere 
    n_sphere = 0
    create_point = lambda : np.array([r.uniform(-rad,rad) for _ in range(d)])
    norm = lambda vec : np.sqrt(functools.reduce(lambda x, y: x + y, map(lambda x: x**2, vec)))
    n_sphere = len(list(filter(lambda x : norm(x) < rad, [create_point() for _ in range(n)])))
    
    # Point_list = np.array([create_point() for i in range(n)])
    # Sphere_list = list(filter(lambda vec : norm(vec) < r))
    # Cube_list = list(filter(lambda vec : norm(vec) >= r))
    return n_sphere/n*(2*rad)**d

def hypersphere_exact(n,d):
    rad = 1
    return (m.pi**(d/2)/m.gamma(d/2+1)*rad**d)
     
def main():
    n = 10000
    d = 11
    print(f"My version: {sphere_volume(n,d)}, Actual: {hypersphere_exact(n,d)}")
    #print(hypersphere_exact(4,1))
    #sphere_volume(n,d)


if __name__ == '__main__':
	main()
