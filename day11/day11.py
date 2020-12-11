import copy

f = 'day11_input.txt'
#f = 'a.txt'
data = open(f,'r').read().split("\n")
width = len(data[0])
height = len(data)

directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

#part 1
def has_neighbours(m, X, Y, allowance):
    count = 0
    state = m[Y][X]
    for direction in directions:
        x = X + direction[0]
        y = Y + direction[1]
        if x < 0 or y < 0 or x == width or y == height:
            continue
        else:
            if m[y][x] == '#':
                count += 1
    if state =='#' and count >= allowance:
        return True
    elif state == 'L' and count == 0:
        return True
    else:
        return False

# part 2
def has_neighbours_new(m, X, Y, allowance):
    count = 0
    state = m[Y][X]
    for direction in directions:
        dist = 1
        while True:
            x = X + direction[0] * dist
            y = Y + direction[1] * dist
            if x < 0 or y < 0 or x == width or y == height:
                break
            else:
                if m[y][x] == '#':
                    count += 1
                    break
                elif m[y][x] == 'L':
                    break
            dist += 1
    
    if state =='#' and count >= allowance:
        return True
    elif state == 'L' and count == 0:
        return True
    else:
        return False

def get_seated(fn, allowance):

    old = copy.deepcopy(data)
    new = [[0 for i in range(width)] for j in range(height)]
    seat_counter = 0
    while True:
        seat_counter = 0
        for y in range(height):
            for x in range(width):
                if old[y][x] == '#':
                    if fn(old, x, y, allowance):
                        new[y][x] = 'L'
                    else:
                        new[y][x] = '#'
                        seat_counter += 1
                elif old[y][x] == 'L':
                    if fn(old, x, y, allowance):
                        new[y][x] = '#'
                        seat_counter += 1
                    else:
                        new[y][x] = 'L'
                else:
                    new[y][x] = '.'
        if old != new:
            old = copy.deepcopy(new)
            new = [[0 for i in range(width)] for j in range(height)]
        else:
            print(seat_counter)
            break
    return 1


get_seated(has_neighbours, 4)
get_seated(has_neighbours_new, 5)
