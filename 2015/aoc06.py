#!/usr/bin/env python

data_in = 'inputs/aoc06.in'

def load(file):
  with open(file) as x: output = x.read()
  return [ol for ol in output.split('\n') if ol]

def gridInit(size, grid = []):
  [grid.append([0] * size) for x in xrange(size)]
  return grid

def solve(data):
  pass

print load(data_in)
