#!/usr/bin/env python

import re, sys

data_in = sys.argv[1] if len(sys.argv[1:]) > 0 else 'inputs/set01/aoc16.in'
mfcsam = {'children': (3, '=', '='), 'cats': (7, '=', '>'), 'samoyeds': (2, '=', '='), 'pomeranians': (3, '=', '<'),
          'akitas': (0, '=', '='), 'vizslas': (0, '=', '='), 'goldfish': (5, '=', '<'), 'trees': (3, '=', '>'),
          'cars': (2, '=', '='), 'perfumes': (1, '=', '=')}
funarr = {'<': lambda x, y: x < y, '>': lambda x, y: x > y, '=': lambda x, y: x == y}

class regex(object):
  def __or__(self, other):
    self.sre = other
    return other
  def group(self, index=0):
    return self.sre.group(index)

def load(file):
  output = []
  rgx = regex()
  with open(file) as x: feed = x.read()
  for line in feed.split('\n'):
    if rgx|re.match(r'Sue \d+: (.*)$', line):
      output.append({k: int(v) for k, v in [line.split(": ") for line in rgx.group(1).split(', ')]})
  return output

def solve(input):
  result = [0, 0]
  lock = [0, 0]
  for sueid, sue in enumerate(input):
    clear = [0, 0]
    for detect in mfcsam:
      if detect in sue:
        if not lock[0]:
          if funarr[mfcsam[detect][1]](sue[detect], mfcsam[detect][0]): result[0] = sueid + 1
          else: clear[0] = 1
        if not lock[1]:
          if funarr[mfcsam[detect][2]](sue[detect], mfcsam[detect][0]): result[1] = sueid + 1
          else: clear[1] = 1
        if clear[0] and clear[1]:
          result = [0, 0]
          break
    else:
        if clear[0]: result[0] = 0
        else: lock[0] = 1
        if clear[1]: result[1] = 0
        else: lock[1] = 1
    if result[0] & result[1]: break
  print "Pt1: {}\nPt2: {}".format(result[0], result[1])

solve(load(data_in))
