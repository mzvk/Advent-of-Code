#!/bin/bash

if [[ $# -lt 1 ]]; then echo "You must specify a day." && exit 1; fi
if [[ ! $1 =~ ^([1-9]|1[0-9]|2[0-5])+$ ]]; then echo "Day must be integer in the range 1 - 25" && exit 1; fi

printf -v DAY "%02d" "$1"
FILE="aoc$DAY.py"

if [[ ! -f "$FILE" ]]; then
  touch $FILE
  chmod +x $FILE
  {
    echo -e '#!/usr/bin/env python\n'
    echo -e 'import sys\n'
    echo -e "data_in = sys.argv[1] if len(sys.argv[1:]) > 0 else 'inputs/set01/aoc$DAY.in'\n"
    echo -e 'def load(file):\n  with open(file) as x: output = x.read()\n  return output\n'
    echo -e 'def solve(data):\n  result = [0, 0]\n  print \"Pt1: {}\\nPt2: {}.format(result[0], result[1])\"\n'
    echo    'solve(load(data_in))'
  } > $FILE
else
  echo "$FILE already exists."
fi
