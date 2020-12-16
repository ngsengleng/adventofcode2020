f = 'day14_input.txt'
data = open(f, 'r').read().split('\n')

mem_size = 36

def get_mem_location(s):
    return int(s[s.find("[")+1:s.find("]")])

def get_components(s):
    return list(map(lambda x: x.strip(), s.split('=')))

def decimal_to_binary(i):
    return str(bin(int(i)))[2:]
            
def floating_binary(s):
    if 'X' not in s:
        yield s
    else:
        yield from floating_binary(s.replace('X', '1', 1))
        yield from floating_binary(s.replace('X', '0', 1))

def p1():
    mask = ''
    mem_dict = {}
    total = 0
    for i in data:
        if 'mask' in i:
            mask = get_components(i)[1]
            continue
        else:
            components = get_components(i)
            memloc = get_mem_location(components[0])
            val = decimal_to_binary(components[1]).zfill(mem_size)
            new_val = [0 for i in range(mem_size)]
            for i in range(mem_size):
                if mask[i] != 'X' and mask[i] != val[i]:
                    new_val[i] = mask[i]
                else:
                    new_val[i] = val[i]
            mem_dict[memloc] = ''.join(new_val)

    for i in mem_dict.values():
        total += int(i, 2)
    print(total)

def p2():
    mask = ''
    mem_dict = {}
    total = 0

    for i in data:
        if 'mask' in i:
            mask = get_components(i)[1]
            continue
        else:
            components = get_components(i)
            memloc = decimal_to_binary(get_mem_location(components[0])).zfill(36)
            val = int(components[1])

            mem_val = ''
            for i in range(mem_size):
                if mask[i] == 'X' or mask[i] == '1':
                    mem_val += mask[i]
                else:
                    mem_val += memloc[i]

            for new_key in floating_binary(''.join(mem_val)):
                mem_dict[new_key] = val

    for i in mem_dict.values():
        total += i
    print(total)
    
p1()
p2()