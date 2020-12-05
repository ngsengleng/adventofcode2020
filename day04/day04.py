import re

dataset = open("day04_input.txt", "r").read().split("\n")
#dataset = ['ecl:gry pid:860033327 eyr:2020 hcl:#fffffd byr:1937 iyr:2017 cid:147 hgt:183cm']
# data dictionary
cat  = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
def datadict(s):
    d = {}
    for x in cat:
        d[x] = 0
    for y in s:
        if y == '':
            continue
        field = str(y[:3])
        if field == 'cid':
            continue
        d[field] = y[4:]
    return d

d_set = []
arr = []
for x in dataset:
    if x == '':
        d_set.append(arr)
        arr = []
    else:
        for y in x.split(' '):
            arr.append(y)
d_set.append(arr)


counter_1 = 0
counter_2 = 0
for x in d_set:
    d = datadict(x)
    # if 0 means dont exist
    if 0 in set(d.values()):
        continue
    else:
        counter_1 += 1
        # byr
        byr = int(d['byr'])
        if byr < 1920 or byr > 2002:
            continue
        
        # iyr
        iyr = int(d['iyr'])
        if iyr < 2010 or iyr > 2020:
            continue
        
        # eyr
        eyr = int(d['eyr'])
        if eyr < 2020 or eyr > 2030:
            continue
        
        # hgt
        hgt = d['hgt']
        val = int(hgt[:-2])
        unit = hgt[-2:]
        if unit == 'cm':
            if val < 150 or val > 193:
                continue
        elif unit == 'in':
            if val < 59 or val > 76:
                continue
        else:
            continue

        # hcl
        hcl = d['hcl']
        if len(hcl) != 7:
            continue
        elif hcl[0] != "#":
            continue
        elif re.search('[g-z]',d['hcl']):
            continue
        
        # ecl
        ecl_set = set(['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'])
        ecl = d['ecl']
        if ecl not in ecl_set:
            continue

        # pid
        pid = d['pid']
        if len(pid) != 9:
            continue

        counter_2 += 1
        

        

print(counter_1, counter_2)
