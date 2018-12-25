#!/usr/bin/env python

data_in = 'inputs/aoc06.in'

def load(file):
  with open(file) as x: output = x.read()
  return [ol for ol in output.split('\n') if ol]

def gridInit():
   grid = []
   for x in xrange(1000):
      grid.append([0] * 1000)
   return grid

def solve(data):
  pass

print load(data_in)
