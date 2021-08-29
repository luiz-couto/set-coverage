import numpy as np

def main():
    # read file
    sizes = input().split()
    num_points = int(sizes[0])
    num_sets = int(sizes[1])

    costs = input().split()

    matrix = np.empty((num_points, num_sets)) 
    for i in range(num_points):
        line = input().split()
        for j in range(num_sets):
            matrix[i][j] = line[j]

    print(costs)
    print(matrix)

if __name__ == "__main__":
    main()