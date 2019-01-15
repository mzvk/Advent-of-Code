#!/usr/bin/env python

import re, sys

data_in = 'inputs/aoc06.in'
action = {'on':     lambda x: [1,        x[1] + 1],
          'off':    lambda x: [0,        x[1] - 1],
          'toggle': lambda x: [x[0] ^ 1, x[1] + 2]}

def load(file):
  with open(file) as x: output = x.read()
  return [ol for ol in output.split('\n') if ol]

def gridInit(size, grid = []):
  [grid.append([[0, 0]] * size) for x in xrange(size)]
  return grid

def parse(dump, grid):
  for instr in dump:
    tmap = re.search(r'^(?:turn )?(off|on|toggle) (\d+),(\d+) through (\d+),(\d+)', instr)
    for y in xrange(int(tmap.group(3)), int(tmap.group(5)) + 1):
      for x in xrange(int(tmap.group(2)), int(tmap.group(4)) + 1):
        grid[y][x] = action[tmap.group(1)](grid[y][x])
        if(grid[y][x][1] < 0): grid[y][x][1] = 0
    return grid

def solve(grid):
  (lit, brit) = (0, 0)
  for y in xrange(1000):
    for x in xrange(1000):
      lit  += grid[y][x][0]
      brit += grid[y][x][1]
  print "Pt1: {}\nPt2: {}".format(lit, brit)

solve(parse(load(data_in), gridInit(1000)))
