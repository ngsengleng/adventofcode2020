dataset = open("day02_input.txt", 'r').read().split("\n")

# part 1
def parse_one(s):
    arr = s.split(" ")
    number = list(map(lambda x: int(x), arr[0].split("-")))
    letter = arr[1]
    pwd = arr[2]
    count = 0
    for i in pwd:
        if i == letter[0]:
            count += 1
    if count < number[0] or count > number[1]:
        return 0
    else:
        return 1


number = 0
for elem in dataset:
    number += parse_one(elem)
print(number)

# part 2
def parse_two(s):
    arr = s.split(" ")
    number = list(map(lambda x: int(x) - 1, arr[0].split("-")))
    letter = arr[1][0]
    pwd = arr[2]
    if ((pwd[number[0]] == letter and pwd[number[1]] != letter) 
        or (pwd[number[0]] != letter and pwd[number[1]] == letter)):
        return 1
    else:
        return 0

number = 0
for elem in dataset:
    number += parse_two(elem)
print(number)