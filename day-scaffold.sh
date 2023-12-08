#!/bin/bash

provided_day="$1"

if ! [ -n "$provided_day" ]; then
    provided_day=$(date +%d)
    echo "No day provided, using current day: $provided_day"
fi

if [ "$provided_day" -lt 1 ] || [ "$provided_day" -gt 25 ]; then
    echo "Invalid day provided. Only 1-25 supported."
    exit 1
fi

slim_day=$(echo $provided_day | sed 's/^0*//')
padded_day=$(printf "%02d" "$slim_day")

echo "Creating puzzle files for day $slim_day..."
mkdir "puzzles/day$padded_day"
touch "puzzles/day$padded_day/common.py"
touch "puzzles/day$padded_day/part1.py"
touch "puzzles/day$padded_day/part2.py"

if ! [ -n "$AOC_SESSION" ]; then
    echo "Hint: if you set the env variable AOC_SESSION with your session cookie, I can get your puzzle input for you."
    exit 0
fi

echo "Downloading input for day $slim_day..."
curl -s -b "session=$AOC_SESSION" -o "$padded_day.input" "https://adventofcode.com/2023/day/$slim_day/input"