#!/usr/bin/env python

data_in = '../inputs/aoc10.in'

def load(file):
  with open(file) as x: output = x.read()
  return output.replace('\n', '')

def look_say(start):
  (current, counter) = ('', 0)
  new = ''
  for digit in start:
    if current != digit:
      if current: new = '{}{}{}'.format(new, counter, current)
      current = digit
      counter = 1
    else: counter += 1
  return '{}{}{}'.format(new, counter, current)

def solve(data):
  start = data
  for x in xrange(50):
    start = look_say(start)
    if x == 39: part1 = len(start)
  print "Pt1:{}\nPt2:{}".format(part1, len(start))

solve(load(data_in))
