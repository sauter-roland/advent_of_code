SPLIT = "^"
EMPTY = "."
START = "S"

try_int = lambda x: int(x) if x.isnumeric() else x

with open('./2025/07/data.txt', 'r') as f:
    graph = f.read()
    graph = graph.replace(START, "1")
    graph = graph.replace(EMPTY, "0")
    graph = graph.splitlines()
    graph_num = []
    for line in graph:
        graph_num.append([try_int(c) for c in line.strip()])

new_graph = []

for idx_row, line in enumerate(graph_num):
    new_line = []
    if idx_row == 0:
        new_graph.append(line)
        continue
    for (idx_col, char) in enumerate(line):
        val = 0
        next_char = line[idx_col + 1] if idx_col + 1 < len(line) else None
        prev_char = line[idx_col - 1] if idx_col - 1 >= 0 else None
        if next_char == SPLIT:
            if isinstance(new_graph[idx_row - 1][idx_col + 1], int):
                val += new_graph[idx_row - 1][idx_col + 1]
        if prev_char == SPLIT:
            if isinstance(new_graph[idx_row - 1][idx_col - 1], int):
                val += new_graph[idx_row - 1][idx_col - 1]
        if char == 0 and isinstance(new_graph[idx_row - 1][idx_col], int):
            val += new_graph[idx_row - 1][idx_col]
        if val > 0:
            new_line.append(val)
        else:
            new_line.append(char)
    new_graph.append(new_line)

print(sum(new_graph[-1]))
