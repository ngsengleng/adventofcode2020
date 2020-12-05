dataset = open('day05_input.txt', 'r').read().split("\n")

# memoized part 1
mem_dict = {}
seat_ids = []
row = 128
col = 8
def get_pos(s, num, min_row, max_row):
    if num == 1:
        if s[0] == 'F' or s[0] == 'L':
            return min_row
        else:
            return max_row
    else:
        if s[0] == 'F' or s[0] == 'L':
            max_row -= num
        else:
            min_row += num
        return get_pos(s[1:], num / 2, min_row, max_row)

biggest = 0
for x in dataset:
    r = 0
    c = 0
    row_map = x[:-3]
    col_map = x[-3:]
    if row_map not in mem_dict:
        mem_dict[row_map] = get_pos(row_map, row / 2, 0, row - 1)
        r = mem_dict[row_map] 
    else:
        r = mem_dict[row_map]
    if col_map not in mem_dict:
        mem_dict[col_map] = get_pos(col_map, col / 2, 0, col - 1)
        c = mem_dict[col_map]
    else:
        c = mem_dict[col_map]

    num = r * 8 + c
    
    seat_ids.append(num)

    if num > biggest:
        biggest = num

print(biggest)

# part 2
# this is O(n^2)
a = sorted(seat_ids)
for i in range(len(a)):
    if a[i + 1] - a[i] == 2:
        print(a[i] + 1)
        break  
