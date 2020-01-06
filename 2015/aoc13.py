#!/usr/bin/env python

import sys, re, copy

data_in = sys.argv[1] if len(sys.argv[1:]) > 0 else 'inputs/set01/aoc13.in'

def load(file):
  guest = {}
  with open(file) as x: output = x.read()
  for line in output.split('\n'):
    pers = re.search(r'([A-Z][a-z]+) would (gain|lose) ([0-9]+) happiness units by sitting next to ([A-Z][a-z]+)\.', line)
    if pers:
      if pers.group(1) not in guest: guest[pers.group(1)] = {pers.group(4): int(pers.group(3)) if pers.group(2) == 'gain' else -int(pers.group(3))}
      else: guest[pers.group(1)].update({pers.group(4): int(pers.group(3)) if pers.group(2) == 'gain' else -int(pers.group(3))})
  return guest

def map_conn(data):
   conn = {}
   for node in data:
      conn[node] = {}
      for neig in data[node]:
         if neig not in conn: conn[neig] = {}
         conn[node].update({neig: (data[node][neig] + data[neig][node])})
         conn[neig].update({node: (data[node][neig] + data[neig][node])})
   return conn

def add_mzvk(data):
   for node in data: data[node].update({'Mzvk': 0})
   data['Mzvk'] = {key:0 for key in data.keys()}
   return data

def osap(graph, current='', visited=None, cost=0, maxh=0, vlist=[]):
   if visited == None: visited = set()
   if current:
      visited.add(current)
      vlist.append(current)
   for next in (set(graph.keys()) - visited):
      maxh = osap(graph, next, visited.copy(), cost+graph[current][next] if current else 0, maxh, copy.deepcopy(vlist))
   if(len(visited) == len(graph.keys())):
      cost += graph[current][vlist[0]]
      maxh = max(maxh, cost)
   return maxh

def solve(data):
  result = []
  data = map_conn(data)
  result.append(osap(data))
  data = add_mzvk(data)
  result.append(osap(data))
  print "Pt1: {}\nPt2: {}".format(result[0], result[1])

solve(load(data_in))
