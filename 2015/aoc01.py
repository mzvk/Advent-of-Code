#!/usr/bin/env python

data_in = 'inputs/aoc01.in'
act = {'(': lambda x: x + 1, ')': lambda x: x - 1}

def load(file):
  with open(file) as x: output = x.read()
  return output

def solve(data):
  (ff, fb) = (0, 0)
  for idx, move in enumerate(data):
    try: ff = act[move](ff)
    except KeyError: pass
    if ff < 0 and not fb: fb = idx + 1
  print "Pt1: {}\nPt2: {}".format(ff, fb)

solve(load(data_in))
