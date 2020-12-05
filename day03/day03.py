forest = list(open("day03_input.txt", "r").read().split("\n"))
height = len(forest)
width = len(forest[0])

# part 1
x = 3
y = 1
count = 0

while (y < height):
    if (x >= width):
        x = x - width
    if forest[y][x] == "#":
        count += 1
    x += 3
    y += 1
print(count)

# part 2
'''
memo = [["-" for i in range(width)] for i in range(height)]

def read(x, y):
    return memo[y][x]

def write(x, y, value):
    memo[y][x] = value
'''
def slope(x, y, count, step_x, step_y):
    if (y >= height):
        return count
    if (x >= width):
        x = x - width
    if forest[y][x] == "#":
        count += 1
    return slope(x + step_x, y + step_y, count, step_x, step_y)

a = slope(0,0,0,1,1)
b = slope(0,0,0,3,1)
c = slope(0,0,0,5,1)
d = slope(0,0,0,7,1)
e = slope(0,0,0,1,2)
print(a*b*c*d*e)
