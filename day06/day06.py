from functools import reduce
data = open("day06_input.txt", "r").readlines()
dataset = []
temp = []
for x in data:
    if x == '\n':
        dataset.append(temp)
        temp = []
    else:
        temp.append(x)
dataset.append(temp)

# part 1
count = reduce(lambda x,y: x + len(set(y)), 
                list(map(lambda x: reduce(lambda y,z: y + z.strip(), x, ''), dataset)), 0)
print(count)

# part 2
count2 = 0
for x in dataset:
    intersect = reduce(lambda a,b: a.intersection(b), list(map(lambda x: set(x.strip()), x)))
    count2 += len(intersect)
print(count2)
