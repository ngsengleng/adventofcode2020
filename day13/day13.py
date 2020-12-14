from math import ceil

f = 'day13_input.txt'

data = open(f, 'r').read().split('\n')
timestamp = int(data[0])
buses = list(map(lambda x: int(x), list(filter(lambda x: x != 'x', data[1].split(',')))))

# part 1
smallest = 'empty'
idx = 0
for i in buses:
    diff = ceil(timestamp / i) * i - timestamp
    if smallest == 'empty' or diff < smallest:
        smallest = diff
        idx = i
print(idx * smallest)

# part 2
# CRT from https://rosettacode.org/wiki/Chinese_remainder_theorem#Python_3.6

from functools import reduce
def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod
 
 
 
def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

# end CRT

a = []
buslist = data[1].split(',')
for i in range(len(buslist)):
    if buslist[i] != 'x':
        a.append(-i % int(buslist[i]))


print(chinese_remainder(buses, a))

