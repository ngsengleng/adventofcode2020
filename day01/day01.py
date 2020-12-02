from itertools import combinations

# dataset
y = open('day01_input.txt', 'r')
x = []
for a in y:
    x.append(int(a))

def sum(a, b, c):
    return a + b + c

# part 1
for i in range(len(x)):
    for j in range(i, len(x)):
        if sum(x[i], x[j], 0) == 2020:
            print(x[i] * x[j])
            break

    

# part 2
for element in combinations(x, 3):
    if sum(element[0], element[1], element[2]) == 2020:
        print(element[0] * element[1] * element[2])
        break
