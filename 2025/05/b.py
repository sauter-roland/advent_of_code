with open('./2025/05/data.txt', 'r') as f:
    lines = f.readlines()

# using a set of all numbers quickly fills up the available RAM T.T
fresh = list()
for line in lines:
    line = line.strip()
    if line == '':
        break
    parts = line.split('-')
    parts = [int(p) for p in parts]
    fresh.append(parts)


fresh = sorted(fresh, key=lambda x: (int(x[0]), int(x[1])))

merged = []
min_start = None
max_end = None
i = 0
while i < len(fresh):
    start, end = fresh[i]
    j = i + 1
    while j < len(fresh):
        start2, end2 = fresh[j]
        if start2 <= end + 1:
            end = max(end, end2)
            j += 1
        else:
            break
    merged.append([start, end])
    i = j

total = 0
for start, end in merged:
    in_range = end - start + 1
    total += in_range
print(total)