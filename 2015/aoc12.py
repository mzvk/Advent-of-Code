#!/usr/bin/env python

data_in = 'inputs/aoc12.in'

def load(file):
  with open(file) as x: output = x.read()
  return output.replace('\n', '')

def solve(data):
  print data
  total = 0
  seq = ''
  for char in data:
    if char == '-': seq = '-'
    else:
      try:
        int(char)
        seq += char
      except ValueError:
        if seq:
          total += int(seq)
          seq = ''
  print "Pt1: {}".format(total)

solve(load(data_in))
