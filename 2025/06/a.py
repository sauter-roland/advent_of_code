with open('./2025/06/data.txt', 'r') as f:
    lines = f.readlines()

numeric = []
for line in lines:
    line = line.strip()
    line = line.split()
    if line[0].isnumeric():
        numeric.append([int(x) for x in line])
    else:
        ops = line
assert len(numeric[0]) == len(ops)

# operations here are only addition and multiplication, which makes this easy
# could just use numpy, but where's the fun in that? ;)
# of course, you'd want to use something vectorized for performance in real life

def product_sum(numbers: list[int]) -> int:
    result = 1
    for n in numbers:
        result *= n
    return result

def solve_column(numbers: list[list[int]], column: int, operation: str) -> int:
    relevant_numbers = [num_list[column] for num_list in numbers]
    if operation == '+':
        return sum(relevant_numbers)
    elif operation == '*':
        return product_sum(relevant_numbers)

results = []
for i in range(len(ops)):
    col_result = solve_column(numeric, i, ops[i])
    results.append(col_result)

print(sum(results))