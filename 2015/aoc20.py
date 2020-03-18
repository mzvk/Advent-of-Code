#!/usr/bin/env python

import sys

data_in = sys.argv[1] if len(sys.argv[1:]) > 0 else 'inputs/set01/aoc20.in'

def load(file):
  with open(file) as x: output = x.read()
  return int(output.replace('\n', ''))

def divs(n):
   divisor = [i for i in xrange(1, int(n ** 0.5) + 1) if not n % i]
   return divisor + [n / d for d in divisor if n != d ** 2]

def solve(data):
  result = [0, 0]
  i = 0
  while not result[0] or not result[1]:
    i += 1
    div = divs(i)
    if not result[0]:
      if sum(div) * 10 >= data: result[0] = i
    if not result[1]:
      if sum(d for d in div if i / d <= 50) * 11 >= data: result[1] = i
  print "Pt1: {}\nPt2: {}".format(result[0], result[1])

solve(load(data_in))
