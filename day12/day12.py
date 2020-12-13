from functools import reduce

f = 'day12_input.txt'

data = open(f,'r').read().split('\n')
# north is positive, south is negative
# east is positive, west is negative

directions = ['N', 'E', 'S', 'W']
# part 1

def get_unit(instr):
    unit = reduce(lambda x,y: x + y, instr[1:])
    return int(unit)

def move(coord, instr):

    direction = instr[0]
    unit = get_unit(instr)
    facing = coord[2]

    if direction == 'N':
        coord[1] += unit
    elif direction == 'S':
        coord[1] -= unit
    elif direction == 'E':
        coord[0] += unit
    elif direction == 'W':
        coord[0] -= unit
    elif direction == 'F':
        return move(coord, [directions[facing], unit])
    
    return coord

def turn_ship(coord, instr):
    direction = instr[0]
    unit = get_unit(instr)
    change = 1 if direction == 'R' else -1

    while unit > 0:
        coord[2] += change
        if coord[2] > 3:
            coord[2] = 0
        elif coord[2] < 0:
            coord[2] = 3
        unit -= 90
    return coord

def p1(ls, coord):
    if ls == []:
        print(coord)
        return

    instr = ls[0]
    direction = instr[0]
    if direction == 'R' or direction == 'L':
        coord = turn_ship(coord, instr)
    else:
        coord = move(coord, instr)
    p1(ls[1:], coord)


p1(data, [0,0,1])

# part 2
def move_ship(ship, waypoint, instr):
    unit = get_unit(instr)
    diff_x = waypoint[0]
    diff_y = waypoint[1]

    ship[0] += diff_x * unit
    ship[1] += diff_y * unit
    
    return ship



def turn_waypoint(coord, instr):
    direction = instr[0]
    unit = get_unit(instr) if direction == 'L' else 360 - get_unit(instr)
    while unit > 0:
        coord[0], coord[1] = coord[1], coord[0]
        coord[0] = -coord[0]
        unit -= 90
    return coord



def p2(ship, waypoint, ls):
    if ls == []:
        print(ship)
        return
    
    instr = ls[0]
    direction = instr[0]
    
    if direction == 'F':
        ship = move_ship(ship, waypoint, instr)
    else:
        if direction == 'R' or direction == 'L':
            waypoint = turn_waypoint(waypoint, instr)
        else:
            waypoint = move(waypoint, instr)
    p2(ship, waypoint, ls[1:])

p2([0,0,1], [10, 1, 1], data)
