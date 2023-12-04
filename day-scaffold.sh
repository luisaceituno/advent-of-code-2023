#!/bin/bash

current_day=$(date +%d)
provided_day="${1:-$current_day}"

if ! [[ $1 =~ ^[0-9][0-9]?$ ]]; then
    echo "No day provided, using current day: $provided_day"
fi

slim_day=$(echo $provided_day | sed 's/^0*//')
padded_day=$(printf "%02s" "$provided_day")

mkdir "puzzles/day$padded_day"
touch "puzzles/day$padded_day/common.py"
touch "puzzles/day$padded_day/part1.py"
touch "puzzles/day$padded_day/part2.py"

if ! [ -n "$AOC_SESSION" ]; then
    echo "Hint: if you set the env variable AOC_SESSION with your session cookie, I can get your puzzle input for you."
    exit 0
fi

curl -b "session=$AOC_SESSION" -o "$padded_day.input" "https://adventofcode.com/2023/day/$slim_day/input"