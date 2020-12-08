f = 'day08_input.txt'
#f = 'a.txt'
data = open(f, 'r').read().split("\n")
import copy

def get_instr(s):
    return s[:3]

def get_num(s):
    return int(s.split(" ")[1])

# part 1
def prog1():
    instr_set = set()
    num  = 0
    ptr = 0
    while ptr not in instr_set:
        instr_set.add(ptr)

        instr = get_instr(data[ptr])
        val = get_num(data[ptr])

        if instr == 'nop':
            ptr += 1
        elif instr == 'acc':
            num += val
            ptr += 1
        else:
            ptr += val
    return num
print(prog1())

# part 2
def prog2(acc, ptr, state, modified):
    if ptr in state:
        return 'infinite', acc
    elif ptr == len(data):
        return 'end', acc
    else:
        this_op = get_instr(data[ptr])
        val = get_num(data[ptr])
        c = copy.deepcopy(state)
        c.add(ptr)

        if modified:
            if this_op == 'nop':
                return prog2(acc, ptr + 1, c, modified)
            elif this_op == 'jmp':
                return prog2(acc, ptr + val, c, modified)
            else: 
                return prog2(acc + val, ptr + 1, c, modified)
        
        else:
            if this_op == 'nop':
                a, b = prog2(acc, ptr + val, c, True)
                if a == 'end':
                    return a, b
                else:
                    return prog2(acc, ptr + 1, c, modified)
            elif this_op == 'jmp':
                a, b = prog2(acc, ptr + 1, c, True)
                if a == 'end':
                    return a, b
                else:
                    return prog2(acc, ptr + val, c, modified)
            else: 
                return prog2(acc + val, ptr + 1, c, modified)

n = set()
a, b = prog2(0, 0, n, False)
print(a,b)

            