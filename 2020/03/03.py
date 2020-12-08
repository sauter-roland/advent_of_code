from typing import List, Tuple
import numpy as np

def readFile(filepath: str) -> List[str]:
    with open(filepath, 'r') as f:
        return f.read().split('\n')

def check_slope(steps_right, steps_down):
    lines = readFile('input_01.txt')

    max_y = len(lines)
    max_x = len(lines[0])
    step = round(steps_right / steps_down)

    positions = [((step*i)%max_x, i) for i in range(0, max_y - 1, steps_down)]
    positions = [lines[p[1]][p[0]] for p in positions]

    print(positions)
    return positions.count('#')

slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]
product = 1
hits = [check_slope(x[0], x[1]) for x in slopes]

for hit in hits:
    product *= hit
print(hits)
print(product)