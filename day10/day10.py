f = 'day10_input.txt'
#f = 'a.txt'
data = list(map(lambda x: int(x), open(f, 'r').read().split('\n')))
data.sort()
builtin = data[-1] + 3

#part 1
ones = 0
threes = 1
if data[0] == 1:
    ones += 1
elif data[0] == 3:
    threes += 1


for i in range(len(data) - 1):
    diff = data[i + 1] - data[i]
    if diff == 1:
        ones += 1
    elif diff == 3:
        threes += 1
print(ones * threes)

# part 2

# preprocessing
adapter_map = {data[-1]: [data[-1] + 3], 0:[]}

for i in range(1, 4):
    if i in data:
        adapter_map[0].append(i)

for i in range(len(data) - 1):
    curr_val = data[i]
    adapter_map[curr_val] = []
    for j in range(1, 4):
        if curr_val + j in data:
            adapter_map[curr_val].append(curr_val + j)

# memoized counting
memo = {}
def find_combi(curr):
    branches = adapter_map[curr]
    if curr == data[-1]:
        return 1
    count = 0
    for i in branches:
        if i not in memo:
            memo[i] = find_combi(i)
        count += memo[i]
    return count

print(find_combi(0))
