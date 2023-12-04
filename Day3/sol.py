import sys
import re
from collections import defaultdict

with open('input.txt') as f:
    matrix = []
    lines = f.readlines()
    for line in lines:
        matrix_line = line.strip()
        
        matrix.append(matrix_line)

    


    def is_valid_coordinate(i, j, rows, cols):
        return 0 <= i < rows and 0 <= j < cols

    def sum_of_adjacent_numbers(engine_schematic):
        rows = len(engine_schematic)
        cols = len(engine_schematic[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]

        total_sum = 0
        for i in range(rows):
            for j in range(cols):
                if engine_schematic[i][j].isdigit():
                    current_sum = int(engine_schematic[i][j])
                    for direction in directions:
                        new_i, new_j = i + direction[0], j + direction[1]
                        if is_valid_coordinate(new_i, new_j, rows, cols) and engine_schematic[new_i][new_j].isdigit():
                            current_sum += int(engine_schematic[new_i][new_j])
                    total_sum += current_sum

        return total_sum

    result = sum_of_adjacent_numbers(matrix)
    print("Il risultato è:", result)