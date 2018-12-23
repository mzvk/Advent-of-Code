#!/usr/bin/env python

import re

data_in = 'inputs/aoc05.in'

def load(file):
  with open(file) as x: output = x.read()
  return [ol for ol in output.split('\n') if ol]

def solve(data):
  total1 = 0
  total2 = 0
  for word in data:
    nice = 0
    nice2 = 0
    if re.search(r'([a-z])\1', word): nice += 1
    if not re.search(r'ab|cd|pq|xy', word): nice += 1
    if re.search(r'[aeiou].*[aeiou].*[aeiou]', word): nice += 1

    if re.search(r'([a-z][a-z]).*\1', word): nice2 += 1
    if re.search(r'([a-z]).\1', word): nice2 += 1

    if nice == 3: total1 += 1
    if nice2 == 2: total2 += 1

  return (total1, total2)

print solve(load(data_in))
