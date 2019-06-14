#!/usr/bin/env python

import re, sys

data_in = sys.argv[1] if len(sys.argv[1:]) > 0 else 'inputs/set01/aoc14.in'
win_sec = 2503

class regex(object):
  def __or__(self, other):
    self.sre = other
    return other
  def group(self, index=0):
    return self.sre.group(index)

class reindeer(object):
  def __init__(self, spd, end, rst):
    self.spd = spd
    self.end = end
    self.rst = rst
    (self.dst, self.stt, self.scr, self.tmr) = (0, 1, 0, self.end)
  def move(self):
    if self.stt: self.dst += self.spd
    self.tmr -= 1
    if not self.tmr:
      self.tmr = self.rst if self.stt else self.end
      self.stt ^= 1
  def score(self):
    self.scr += 1

def load(file):
  with open(file) as x: data = x.read()
  output = []
  rgx = regex()
  for line in data.split('\n'):
    if rgx|re.match(r'\w+ can fly ([0-9]+) km/s for ([0-9]+) seconds, but then must rest for ([0-9]+) seconds\.$', line):
      output.append(reindeer(int(rgx.group(1)), int(rgx.group(2)), int(rgx.group(3))))
  return output

def solve(rndl):
  high = [0, 0]
  for x in xrange(win_sec):
    leader = []
    for idx, rnd in enumerate(rndl):
      rnd.move()
      if rnd.dst > high[0]:
        high[0] = rnd.dst
        leader = [idx]
      elif rnd.dst == high[0]: leader.append(idx)
    [rndl[x].score() for x in leader]

  high[1] = 0
  for rnd in rndl:
    if high[1] < rnd.scr: high[1] = rnd.scr

  print "Pt1: {}".format(high[0])
  print "Pt2: {}".format(high[1])

solve(load(data_in))
