#!/usr/bin/env python

import re, sys

data_in = 'inputs/aoc07.in'
data = {}

def load(file):
  with open(file) as x: output = x.read()
  return dict(reversed(line.split(' -> ')) for line in [ol for ol in output.split('\n') if ol])

def gates(operand, args):
   if operand == 'AND':     return solve(args[0]) & solve(args[1])
   if operand == 'OR':      return solve(args[0]) | solve(args[1])
   if operand == 'LSHIFT':  return (solve(args[0]) << int(args[1])) & 0xFFFF
   if operand == 'RSHIFT':  return (solve(args[0]) >> int(args[1])) & 0xFFFF
   if operand == 'NOT':     return ~ solve(args[0]) + 2 ** 16
   print "-- !FAILED TO ASSERT GATE TYPE! --"
   sys.exit()

def solve(key):
   try:
      return int(key)
   except ValueError:
      pass

   try:
      return int(data[key])
   except ValueError:
      rgx = re.search(r'^([0-9a-z]+)?(?: )?(NOT|AND|OR|[LR]SHIFT) ([0-9a-z]+)$', data[key])
      if rgx:
         data[key] = gates(rgx.group(2), [value for value in rgx.groups()[::2] if not value == None])
         return data[key]
      else: return solve(data[key])

data = load(data_in)
print "Circiut a = {}".format(solve('a'))
