#!/usr/bin/env python

data_in = 'inputs/aoc11.in'

def load(file):
  with open(file) as x: output = x.read()
  return output.replace('\n', '')

print load(data_in)
