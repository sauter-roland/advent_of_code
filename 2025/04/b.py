import numpy as np


def read_data_to_np(path: str) -> np.ndarray:
    with open(path, 'r') as f:
        lines = f.readlines()
    lines = [line.strip() for line in lines]
    lines = [line.replace('@', '1').replace('.', '0') for line in lines]
    int_lines = [[int(char) for char in line] for line in lines]
    data = np.array(int_lines)
    return data


def get_neighbors(data: np.ndarray, row: int, col: int) -> int:
    empty_neighbors = []
    n_rows, n_cols = data.shape
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            idx_i = row + i
            idx_j = col + j
            if i == 0 and j == 0:
                continue
            if idx_i < 0 or idx_j < 0:
                empty_neighbors.append(0)
                continue
            if idx_i >= n_rows or idx_j >= n_cols:
                empty_neighbors.append(0)
                continue
            point = data[idx_i, idx_j]
            empty_neighbors.append(point)
    return sum(empty_neighbors)


data = read_data_to_np("./04/data.txt")
removed = 0
while True:
    total = 0
    for top_i, row in enumerate(data):
        for top_j, col in enumerate(row):
            result = get_neighbors(data, top_i, top_j)
            if result < 4 and data[top_i, top_j] == 1:
                data[top_i, top_j] = 0
                total += 1
    removed += total
    if total == 0:
        break

print(removed)