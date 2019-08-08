import re

data_in = '../inputs/aoc11.in'

def load(file):
  with open(file) as x: output = x.read()
  return output.replace('\n', '')

alph = 'abcdefghijklmnopqrstuvwxyz'
badc = ['i', 'o', 'l']
badn = ['h', 'n', 'k']

def valid(data):
  data = list(data)
  temp = data
  inc = 0
  for idx, char in enumerate(temp):
    if inc: data[idx] = 'a'
    if char in badc and not inc:
	  data[idx] = alph[(ord(char) - 97 + 1) % len(alph)]
	  inc = 1
  return ''.join(data)

def straigth(data):
  for idx, char in enumerate(data):
    if idx >= len(data) - 3: return 0
    if ord(data[idx]) - ord(data[idx + 1]) == -1 and ord(data[idx + 1]) - ord(data[idx + 2]) == -1: return 1

def inc(data, pos = 0, step = 1):
  data = list(reversed(data))
  if data[pos] in badn: step = 2
  data[pos] = alph[(ord(data[pos]) - 97 + step) % len(alph)]
  return inc(''.join(reversed(data)), pos + 1) if data[pos] == 'a' and pos < 7 else ''.join(reversed(data)) 

password = valid(load(data_in))
result = [0, 0]

while True:
  password = inc(password)
  if re.search(r'([a-z])\1.*((?!\1)[a-z])\2', password) and straigth(password): break
result[0] = password

while True:
  password = inc(password)
  if re.search(r'([a-z])\1.*((?!\1)[a-z])\2', password) and straigth(password): break
result[1] = password

print "Pt1: {}\nPt2: {}".format(result[0], result[1])
