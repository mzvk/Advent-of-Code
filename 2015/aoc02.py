#!/usr/bin/env python

import sys

data_in = sys.argv[1] if len(sys.argv[1:]) > 0 else 'inputs/set01/aoc02.in'

def load(file):
  with open(file) as x: output = x.read()
  return [ol for ol in output.split('\n') if ol]

def solve(data):
  (tp, rb) = (0, 0)
  for pkg in data:
    pkg = sorted([int(val) for val in pkg.split('x')])
    tp += 2*pkg[0]*pkg[1] + 2*pkg[0]*pkg[2] + 2*pkg[1]*pkg[2] + pkg[0]*pkg[1]
    rb += 2*pkg[0] + 2*pkg[1] + pkg[0]*pkg[1]*pkg[2]
  print "Pt1: {}\nPt2: {}".format(tp, rb)

solve(load(data_in))
