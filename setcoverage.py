import numpy as np

class SetCoverage:
    def __init__(self, num_points, num_sets, costs, matrix):
        self.num_points = num_points
        self.num_sets = num_sets
        self.costs = costs
        self.matrix = matrix
        
        self.used_sets = np.zeros(num_sets)
        self.points_values = np.zeros(num_points)
        self.covered_points = np.zeros(num_points)

    def next_uncovered_point(self):
        for i in range(len(self.covered_points)):
            if self.covered_points[i] == 0:
                return (i, False)
        
        return (-1, True)

    def sum_points_in_set(self, set):
        total = 0
        set_column = self.matrix[:, set]
        for i in range(len(set_column)):
            point = set_column[i]
            if point == 1:
                total += self.points_values[i]
        
        return total

    def get_point_value_and_set(self, point):
        min_value = -1
        selected_set = -1

        point_line = self.matrix[point, :]
        for i in range(len(point_line)):
            set = point_line[i]
            if set == 1:
                total = self.sum_points_in_set(i)
                max_cost = self.costs[i]

                value = max_cost - total
                if min_value == -1 or value < min_value:
                    min_value = value
                    selected_set = i

        return (min_value, selected_set)

    def update_used_sets(self, set):
        self.used_sets[set] = 1
        
        set_column = self.matrix[:, set]
        for i in range(len(set_column)):
            point = set_column[i]
            if point == 1:
                self.covered_points[i] = 1
    
    def printArray(self, arr):
        for item in arr:
            print( ('%f' % round(item, 7)).rstrip('0').rstrip('.'), end=" ")
        print()

    def run(self):
        next_point, all_covered = self.next_uncovered_point()
        if all_covered:
            self.printArray(self.used_sets)
            self.printArray(self.points_values)
            return
        
        value, set = self.get_point_value_and_set(next_point)
        self.points_values[next_point] = value

        self.update_used_sets(set)
        self.run()