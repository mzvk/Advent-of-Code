#!/usr/bin/env python

data_in = 'inputs/aoc04.in'

import hashlib

def in_generator():
  counter = 0
  while(True):
    counter += 1
    yield str(counter)
    
input = 'yzbqklnj'
hash = in_generator()

while(True):
  out = hash.next()
  if(hashlib.md5("{}{}".format(input, out)).hexdigest()[:5] == '00000'): 
    print out
    break
