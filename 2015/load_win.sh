#!/bin/bash --

function join { local IFS="$1"; shift; echo "$*"; }

cset=01
cdys=1
cdye=25

while (($#)); do
  if   [[ $1 =~ ^set=([0-9]{1,2})$ ]]; then
    printf -v cset "%02d" "${BASH_REMATCH[1]}"
  elif [[ $1 =~ ^set=all$ ]]; then
    cset=all
  elif [[ $1 =~ ^day=([0-9]{1,2}(-[0-9]{1,2})?)$ ]]; then
    arrIN=(${BASH_REMATCH[1]//-/ })
  elif [[ $1 =~ ^day=all$ ]]; then
    cdys=1
    cdye=25
  elif [[ $1 =~ ^day=$ ]]; then
    0
  else
    echo -e "\e[31m[!]\e[0m Ignored unknown or misused argument \"$1\"."
  fi
  shift
done

if [[ $cset == "all" ]]; then

   exit

else
  if [[ -f outputs/set$cset ]]; then
    mapfile -t eth < <(cat outputs/set$cset)
  else
    echo -e "\e[31m[!]\e[0m No set with id $cset found."
    exit
  fi
fi

echo -e """
Exection time legend:
\033[31m > 1s \033[0m
\033[33m > 250ms \033[0m
"""

for day in {1..25}; do
  printf -v sday "%02d" $day
  if [[ "${eth[((day - 1))]})" =~ "x x" ]]; then
     start=0
     end=0
     sts="\e[33m.\e[0m"
  else
    start=$(date +%s%3N)
    output=$(join " " $(python aoc$sday.py | sed -r 's/(Pt[12]: |\n)//g'))
    end=$(date +%s%3N)
    [[ "${output[@]}" == "${eth[((day - 1))]}" ]] && sts="\e[92m+\e[0m" || sts="\e[31m-\e[0m"
  fi
  exect=$((end-start))
  if [[ $exect -gt 1000 ]]; then
    exect="\033[31m$((exect/1000))s\033[0m"
  elif [[ $exect -gt 200 ]]; then
    exect="\033[33m"$exect"ms\033[0m"
  else
    exect=$exect"ms"
  fi
  echo -e "2015 Day$sday (set$cset: [$sts]) execution: $exect"
done
