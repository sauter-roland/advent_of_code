with open("./2025/06/data.txt", "r") as f:
    lines = f.readlines()
    lines = [list(line) for line in lines]

ops = lines.pop()

def transpose(matrix: list[list[str]]) -> list[list[str]]:
    transverse = [[] for _ in range(len(matrix[0]))]
    for line in matrix:
        for (jdx, char) in enumerate(line):
            transverse[jdx].append(char)
    return transverse


def product_sum(numbers: list[int]) -> int:
    result = 1
    for n in numbers:
        result *= n
    return result


def do_calculation(op: str, numbers: list[int]) -> int:
    if op == "+":
        return sum(numbers)
    elif op == "*":
        return product_sum(numbers)
    raise ValueError(f"Unknown operation: {op}")

transverse = transpose(lines)
transverse.pop() # remove newline column

current_op = None
current_numbers = []
results = []
for (idx, op) in enumerate(ops):
    if op != " ":
        current_op = op
    is_empty = all(char == " " for char in transverse[idx])
    if is_empty:
        result = do_calculation(current_op, current_numbers)
        results.append(result)
        current_numbers = []
        current_op = None
    else:
        number_str = "".join(transverse[idx]).strip()
        current_numbers.append(int(number_str))
result = do_calculation(current_op, current_numbers)
results.append(result)

print(sum(results))
