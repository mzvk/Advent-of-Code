#!/usr/bin/env python

import re, sys

data_in = sys.argv[1] if len(sys.argv[1:]) > 0 else 'inputs/set01/aoc05.in'

def load(file):
  with open(file) as x: output = x.read()
  return [ol for ol in output.split('\n') if ol]

def solve(data):
  output = [0, 0]
  for word in data:
    if re.search(r'([a-z])\1', word) and not re.search(r'ab|cd|pq|xy', word) and re.search(r'[aeiou].*[aeiou].*[aeiou]', word): output[0] += 1
    if re.search(r'([a-z]{2}).*\1', word) and re.search(r'([a-z]).\1', word): output[1] += 1
  print "Pt1: {}\nPt2: {}".format(output[0], output[1])

solve(load(data_in))
