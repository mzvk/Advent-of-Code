#!/usr/bin/env python

data_in = 'inputs/aoc01.in'
act = {'(': lambda x: x + 1, ')': lambda x: x - 1}

def load(file):
  with open(file) as x: output = x.read()
  return output

def solve(data):
  floor = 0
  for move in data:
    try: floor = act[move](floor)
    except KeyError: pass
  return floor

print solve(load(data_in))
