from itertools import combinations
from functools import reduce

f = 'day09_input.txt'
data = list(map(lambda x: int(x), open(f, 'r').read().split('\n')))

coords = [0, 25]
target = 0

# part 1
while True:
    head = coords[0]
    tail = coords[1]

    sumlist = set(map(lambda x: sum(x), list(combinations(data[head:tail], 2))))
    if data[tail] not in sumlist:
        target = data[tail]
        print(data[tail])
        break
    else:
        coords = list(map(lambda x: x + 1, coords))


# part 2
window = []
i = 0
while i < len(data):
    
    while sum(window) > target:
        window.pop(0)
    if sum(window) == target:
        break
    window.append(data[i])
    
    i += 1
print(min(window) + max(window))