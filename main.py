import numpy as np
from setcoverage import *

def main():
    # read file
    sizes = input().split()
    num_points = int(sizes[0])
    num_sets = int(sizes[1])

    costs = input().split()
    for i in range(len(costs)):
        costs[i] = int(costs[i])

    matrix = np.empty((num_points, num_sets)) 
    for i in range(num_points):
        line = input().split()
        for j in range(num_sets):
            matrix[i][j] = line[j]

    # print(costs)
    # print(matrix)

    set_coverage = SetCoverage(num_points, num_sets, costs, matrix)
    set_coverage.run()

if __name__ == "__main__":
    main()