# bags are in format (number, desc, color)
# bags that contain no other bags are in format (no, other) : 'end'
import nltk
from nltk import tokenize
# nltk.download('punkt')
# requires installation of nltk and corresponding libary

data = open('day07_input.txt', 'r').read().split('\n')

bag_map = {}

# tokenizing input and processing tokens
for x in data:
  sent_token = tokenize.word_tokenize(x)
  first_bag = False
  head = ''
  for i in range(len(sent_token)):
    token = sent_token[i]
    # look for occurences of bag
    if token == 'bag' or token == 'bags':
      col_pair = (sent_token[i - 2], sent_token[i - 1])
      # if is first bag encountered
      if first_bag == False:
        bag_map[col_pair] = []
        head = col_pair
        first_bag = True
      else:
        if col_pair == ('no', 'other'):
          bag_map[head].append('end')
        else:
          subsq_pair = (sent_token[i - 3], sent_token[i - 2], sent_token[i - 1])
          bag_map[head].append(subsq_pair)

# part 1

def get_desc(s):
  return (s[-2], s[-1])

def traverse(idx, look_for):
  ls = bag_map[idx]
  if 'end' in ls:
    return 0
  else:
    for i in ls:
      key = get_desc(i)
      if key == look_for:
        return 1
      else:
        if traverse(key, look_for) == 1:
          return 1
    return 0

count = 0
for x in bag_map.keys():
  count += traverse(x, ('shiny', 'gold'))
print(count)

# part 2
def get_num(s):
  return int(s[0])

def counter(idx):
  ls = bag_map[idx]
  if 'end' in ls:
    return 0
  else:
    count = 0
    for i in ls:
      key = get_desc(i)
      num = get_num(i)
      count += num + counter(key) * num
    return count

a = ('shiny', 'gold')
print(counter(a))
