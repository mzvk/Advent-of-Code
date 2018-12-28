#!/usr/bin/env python

data_in = 'inputs/aoc08.in'

def load(file):
  with open(file) as x: output = x.read()
  return [ol for ol in output.split('\n') if ol]

data = load(data_in)

(tmem, tstr, tnst) = (0, 0, 0)
for line in data:
  tstr += len(line)
  tmem += len(line.decode('string_escape')) - 2
  tnst += len(repr(line.replace(r'"', r'."')))
#  tmem += len(repr(line.replace(r'\"', r'\."'))) + 2

print "Total chars of str: {} [23]".format(tstr)
print "Total chars in mem: {} [11]".format(tmem)
print "Total new repr:     {} [xx]".format(tnst)
print "String literals overhead 1: {}".format(tstr - tmem)
print "String literals overhead 2: {}".format(tnst - tstr)
