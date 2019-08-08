#!/usr/bin/env python

import re, sys

data_in = sys.argv[1] if len(sys.argv[1:]) > 0 else 'inputs/set01/aoc09.in'

def load(file):
  output = {}
  with open(file) as x: nodes = x.read()
  for line in nodes.split('\n'):
    matchex = re.match(r'([A-Za-z]+) to ([A-Za-z]+) = ([0-9]+)', line)
    if matchex:
      if matchex.group(1) not in output: output[matchex.group(1)] = {matchex.group(2): int(matchex.group(3))}
      else: output[matchex.group(1)][matchex.group(2)] = int(matchex.group(3))
      if matchex.group(2) not in output: output[matchex.group(2)] = {matchex.group(1): int(matchex.group(3))}
      else: output[matchex.group(2)][matchex.group(1)] = int(matchex.group(3))
  return output

def scpp(graph, current='', visited=None, cost=0, min=65535, max=0):   ## Santa Claus Path Protocol
   if visited == None: visited = set()
   if current: visited.add(current)
   for next in (set(graph.keys()) - visited):
      (min, max) = scpp(graph, next, visited.copy(), cost+graph[current][next] if current else cost, min, max)
   if(len(visited) == len(graph.keys())):
      if cost < min: min = cost
      if cost > max: max = cost
   return (min, max)

result = scpp(load(data_in))
print "Pt1: {}\nPt2: {}".format(result[0], result[1])
