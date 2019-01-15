#!/usr/bin/env python

import re, sys

data_in = 'inputs/aoc09.in'

class node(object):
  def __init__(self, id):
    self.id = id
    self.neig = {}
  def addN(self, neigh, cost):
    self.neig[neigh] = cost
  def sM(self):
    for n in self.neig:
      pass
#      print "-- {}: {}".format(n, self.neig[n])

def load(file):
  with open(file) as x: output = x.read()
  return [ol for ol in output.split('\n') if ol]

def lsdb(data):
  lsdb = {}
  for line in data:
    feed = re.search(r'^([A-Za-z]+) to ([A-Za-z]+) = ([0-9]+)', line)
    if feed.group(1) not in lsdb: lsdb[feed.group(1)] = node('new')
    lsdb[feed.group(1)].addN(feed.group(2), feed.group(3))
  return lsdb

nodes = lsdb(load(data_in))
#for n in  nodes:
#  print "Node: {}".format(n)
#  nodes[n].sM()
