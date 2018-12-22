#!/usr/bin/env python

data_in = 'inputs/aoc04.in'

import hashlib, sys

sufix = lambda s = 0: (str(s + 1*x) for x, _ in enumerate(iter(int, 1)))
progress = '\|/-\|/-'

solution = {5: '', 6: ''}
	
input = 'yzbqklnj'

for value in sufix():
  if(hashlib.md5("{}{}".format(input, value)).hexdigest()[:5] == '0' * 5 and not solution[5]):
    sys.stdout.write("\r ** five 0's solution found **\n")
    sys.stdout.flush()
    solution[5] = value

  if(hashlib.md5("{}{}".format(input, value)).hexdigest()[:6] == '0' * 6 and not solution[6]): 
    sys.stdout.write("\r ** six 0's solution found **\n")
    sys.stdout.flush()  
    solution[6] = value	
  
  if(solution[5] and solution[6]): break
  sys.stdout.write("\r [{}] {}".format(progress[int(value) % 8], value))
  sys.stdout.flush()

print "Pt1: {}\nPt2: {}".format(solution[5], solution[6])
