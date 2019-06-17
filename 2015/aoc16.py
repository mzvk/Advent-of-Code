#!/usr/bin/env python

import re

data_in = "inputs/aoc16.in"
mfcsam = {'children': 3, 'cats': 7, 'samoyeds': 2, 'pomeranians': 3, 'akitas': 0, 'vizslas': 0, 'goldfish': 5, 'trees': 3, 'cars': 2, 'perfumes': 1}

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
  for sueid, sue in enumerate(input):
    notsue = 1
    for detect in mfcsam:
      if detect in sue:
        if not mfcsam[detect] == sue[detect]: notsue = 0
    if notsue: break
  print sueid + 1

solve(load(data_in))
