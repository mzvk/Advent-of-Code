#!/usr/bin/env python

data_in = 'inputs/aoc04.in'

import hashlib

def in_generator(c = 0):
  while(True):
    c += 1
    yield str(c)

solution = {5: '', 6: ''}
	
input = 'yzbqklnj'
hash = in_generator()

while(True):
  out = hash.next()
  if(hashlib.md5("{}{}".format(input, out)).hexdigest()[:5] == '00000' and not solution[5]): 
    solution[5] = out
  if(hashlib.md5("{}{}".format(input, out)).hexdigest()[:6] == '000000' and not solution[6]): 
    solution[6] = out
  if(solution[5] and solution[6]): break

print "Pt1: {}\nPt2: {}".format(solution[5], solution[6])
