with open('./2025/07/data.txt', 'r') as f:
    graph = f.readlines()
    graph = [line.strip() for line in graph]

SPLIT = '^'
BEAM = '|'
EMPTY = '.'
START = 'S'

new_graph = []
for (idx_row, line) in enumerate(graph):
    new_line = []
    if idx_row == 0:
        new_graph.append(line)
        continue
    for (idx_col, char) in enumerate(line):
        next_char = line[idx_col + 1] if idx_col + 1 < len(line) else None
        prev_char = line[idx_col - 1] if idx_col - 1 >= 0 else None
        if (
            (next_char == SPLIT and new_graph[idx_row - 1][idx_col + 1] == BEAM)
            or (prev_char == SPLIT and new_graph[idx_row - 1][idx_col - 1] == BEAM)
        ):
            new_line.append(BEAM)
        elif (
            (char == EMPTY and new_graph[idx_row - 1][idx_col] == BEAM)
            or (char == EMPTY and new_graph[idx_row - 1][idx_col] == START)
        ):
            new_line.append(BEAM)
        else:
            new_line.append(char)
    new_graph.append(''.join(new_line))

total = 0
for (row_idx, line) in enumerate(new_graph):
    for col_idx, char in enumerate(line):
        if char == SPLIT and new_graph[row_idx - 1][col_idx] == BEAM:
            total += 1
print(total)


