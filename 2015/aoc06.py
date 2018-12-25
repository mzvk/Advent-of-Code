#!/usr/bin/env python

import re

data_in = 'inputs/aoc06.in'
act = {'on':  lambda x: x + 1, 'off': lambda x: x - 1, 'toggle':   lambda x: x + 2}

def load(file):
  with open(file) as x: output = x.read()
  return [ol for ol in output.split('\n') if ol]

def gridInit(size, grid = []):
  [grid.append([0] * size) for x in xrange(size)]
  return grid

def solve(data):
  grid = gridInit(1000)
  for action in data:
    action = re.search(r'^(?:turn )?(off|on|toggle) (\d+),(\d+) through (\d+),(\d+)', action)
    
    
print load(data_in)
