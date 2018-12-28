#!/usr/bin/env python

data_in = 'inputs/aoc08.in'

def load(file):
  with open(file) as x: output = x.read()
  return [ol for ol in output.split('\n') if ol]

def solve(data):
  (tmem, tstr, tnst) = (0, 0, 0)
  for line in data:
    tstr += len(line)
    tmem += len(line.decode('string_escape')) - 2
    tnst += len(repr(line.replace(r'"', r'."')))
  print "Pt1: {}\nPt2: {}".format(tstr - tmem, tnst - tstr)

solve(load(data_in))
