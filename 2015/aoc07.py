#!/usr/bin/env python

import re, sys

data_in = 'inputs/aoc07.in'
data = {}
gates = {'AND':    lambda args: circuit(args[0]) & circuit(args[1]),
         'OR':     lambda args: circuit(args[0]) | circuit(args[1]),
         'LSHIFT': lambda args: (circuit(args[0]) << int(args[1])) & 0xFFFF,
         'RSHIFT': lambda args: (circuit(args[0]) >> int(args[1])) & 0xFFFF,
         'NOT':    lambda args: ~ circuit(args[0]) + 2 ** 16}

def load(file):
  with open(file) as x: output = x.read()
  return dict(reversed(line.split(' -> ')) for line in [ol for ol in output.split('\n') if ol])

def circuit(key):
  try:
    return int(key)
  except ValueError:
    try:
      return int(data[key])
    except ValueError:
      rgx = re.search(r'^([0-9a-z]+)?(?: )?(NOT|AND|OR|[LR]SHIFT) ([0-9a-z]+)$', data[key])
      if rgx:
        try:
          data[key] = gates[rgx.group(2)]([value for value in rgx.groups()[::2] if not value == None])
        except KeyError:
          print '-- !FAILED TO ASSERT GATE TYPE! --'
          sys.exit()
        return data[key]
      else: return circuit(data[key])

def solve(cache):
  global data
  output = []
  data = cache.copy()
  output.append(circuit('a'))
  data = cache.copy()
  data['b'] = output[0]
  output.append(circuit('a'))
  print "Pt1: {}\nPt2: {}".format(output[0], output[1])

solve(load(data_in))
