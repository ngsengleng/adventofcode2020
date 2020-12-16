f = 'day15_input.txt'
data = list(map(lambda x: int(x), open(f, 'r').read().split(',')))


def find_turn(num):
    mem_dict = {0:[]}
    prev_num = 0
    current_turn = 1

    for i in data:
        mem_dict[i] = [current_turn]
        current_turn += 1
        prev_num = i

    while current_turn != num + 1:
        if prev_num not in mem_dict:
            prev_num = 0
        else:
            if len(mem_dict[prev_num]) == 1:
                prev_num = 0
            else:
                most_recent = mem_dict[prev_num][-1]
                second_most = mem_dict[prev_num][-2]
                prev_num = most_recent - second_most
        if prev_num not in mem_dict:
            mem_dict[prev_num] = []
        mem_dict[prev_num].append(current_turn)
        current_turn += 1


    print(prev_num)

find_turn(2020)
find_turn(30000000)