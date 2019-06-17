#!/usr/bin/env python

import re

data_in = 'inputs/aoc11.in'
alph = 'abcdefghijklmnopqrstuwvxyz'

def load(file):
  with open(file) as x: output = x.read()
  return output.replace('\n', '')

def solve(data):
  s = list(data)
  s = rmbad(s)

def rmbad(s):
  for char in s:
    pass

def straight(s):
  for idx in xrange(len(s)):
    if idx + 3 >= len(s): return 0
    if not ord(s[idx]) > 120:
      if ord(s[idx]) == ord(s[idx+1])-1 and ord(s[idx+1]) == ord(s[idx+2])-1:
        return 1

string = load(data_in)
string = 'ghijklmn'

while True:
  new = []

  for idx, char in enumerate(reversed(string)):
    shft = 2 if char == 'h' or char == 'n' or char == 'k' else 1
    new.append(alph[(ord(char) - 97 + shft) % len(alph)])
    if not new[idx] == 'a': break

  string = "{}{}".format(string[:len(string) - (1 + idx)], ''.join(reversed(new)))
  if re.search(r'([a-z])\1((?!\1)[a-z])\2', string) and straight(string) and not re.search(r'[iol]', string): break


print string
