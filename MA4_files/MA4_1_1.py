
"""
Solutions to module 4
Review date:
"""

student = "Alexander Hedene"
reviewer = ""


import random as r
import matplotlib.pyplot as plt
import math

def approximate_pi(n):
    circle_list_x = []
    circle_list_y = []
    square_list_x = []
    square_list_y = []
    n_c = 0
    for i in range(n):
        point = [r.uniform(-1,1), r.uniform(-1,1)]
        if (point[0]**2 + point[1]**2)**0.5 < 1:
            circle_list_x.append(point[0])
            circle_list_y.append(point[1])
            n_c += 1
        else:
            square_list_x.append(point[0])
            square_list_y.append(point[1])
    
    plt.scatter(circle_list_x, circle_list_y, s=0.5, c="red")
    plt.scatter(square_list_x, square_list_y, s=0.5, c="blue")
    # plt.title('Monte carlo approximation of pi')
    # plt.xlabel('X')
    # plt.ylabel('Y')
    # plt.legend(["Points inside circle", "Points outside cirle"])
    plt.savefig(f"Scatter_plot_n_{n}")
    
    pi_approx = 4*n_c/n
    # print(f"Total number of points {n}, with {n_c} points inside circle")
    # print(f"Approximated value of pi: {pi_approx:.5f}\nActual value of pi: {math.pi:.5f}\n")
    return pi_approx
    
def main():
    dots = [1000, 10000, 100000]
    for n in dots:
        approximate_pi(n)

if __name__ == '__main__':
	main()
