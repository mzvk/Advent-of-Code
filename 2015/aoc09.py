#!/usr/bin/env python

import re, sys

data_in = 'inputs/aoc09.in'
data_in = 'inputs/aoc09.test'

class graph(object):
  def __init__(self, data):
    self.nodes = {}
    self.lsdb(data)
    self.sp = 0
  def lsdb(self, data):
    for line in data:
      grp = re.search(r'^([A-Za-z]+) to ([A-Za-z]+) = ([0-9]+)', line)
      if grp.group(1) not in self.nodes: self.nodes[grp.group(1)] = node()
      if grp.group(2) not in self.nodes: self.nodes[grp.group(2)] = node()
      self.nodes[grp.group(1)].add(grp.group(2), grp.group(3))
      self.nodes[grp.group(2)].add(grp.group(1), grp.group(3))
  def mst(self):
    for nd in self.nodes:
      visited = set([nd])
      root = nd
      next = ''
      (cost, path) = (0, 0)
#      print "Root: {}".format(nd)
      for _ in xrange(len(self.nodes)):
        next = ''
        cost = 0
        for nn in self.nodes[root].neig:
#          print "{} -> {}: {}".format(nd, nn, self.nodes[root].neig[nn])
          if nn not in visited:
            if not cost:
              cost = self.nodes[root].neig[nn]
              next = nn
            elif self.nodes[nd].neig < cost:
              cost = self.nodes[root].neig[nn]
              next = nn
        visited.add(next)
        root = next
        path += cost
      if not self.sp: self.sp = path
      elif self.sp > path: self.sp = path
    print self.sp

  def dump(self):
    for city in self.nodes:
      print city
      self.nodes[city].dump()

class node(object):
  def __init__(self):
    self.neig = {}
  def add(self, neigh, cost):
    self.neig[neigh] = int(cost)
  def dump(self):
    print self.neig

def load(file):
  with open(file) as x: output = x.read()
  return [ol for ol in output.split('\n') if ol]

graph = graph(load(data_in))
graph.mst()

graph.dump()
