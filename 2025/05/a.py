with open('./2025/05/data.txt', 'r') as f:
    lines = f.readlines()

# using a set of all numbers quickly fills up the available RAM T.T
fresh = list()
ingredients = list()
is_range = True
for line in lines:
    line = line.strip()
    if line == '':
        is_range = False
        continue
    if is_range:
        start, end = line.split('-')
        start = int(start)
        end = int(end)
        start_end = (start, end)
        fresh.append(start_end)
    else:
        ingredients.append(int(line))

total_fresh = 0
for ingredient in ingredients:
    for fresh_range in fresh:
        start, end = fresh_range
        if start <= ingredient <= end:
            total_fresh += 1
            break

print(total_fresh)