from dataclasses import dataclass
from functools import cache

@dataclass
class Record:
    line: str
    ranges: list[int]

    @property
    def known_damaged(self):
        return len([c for c in self.line if c == "#"])

    def more_damaged(self):
        return self.known_damaged < sum(self.ranges)

@cache
def recurse(remaining_string, remaining_ranges, current_streak):
    possibilities = 0
    if len(remaining_string) == 0:
        if not current_streak and len(remaining_ranges) == 0:
            return 1
        if len(remaining_ranges) == 1 and current_streak == remaining_ranges[0]:
            return 1
        return 0
    if len(remaining_ranges) == 0:
        if all([c in [".", "?"] for c in remaining_string]):
            return 1
        return 0
    target_streak = remaining_ranges[0]
    current_char = remaining_string[0]
    if current_char == "#":
        # add to current streak, continue
        possibilities += recurse(remaining_string[1:], remaining_ranges,  current_streak+1)
    if current_char == ".":
        if current_streak:
            if current_streak != target_streak:
                # couldn't complete streak
                return 0
            # could complete streak
            possibilities += recurse(remaining_string[1:], remaining_ranges[1:], 0)
        if not current_streak:
            # not in a streak, continue
            possibilities += recurse(remaining_string[1:], remaining_ranges, 0)
    if current_char == "?":
        if current_streak == target_streak:
            # streak complete, continue
            possibilities += recurse(remaining_string[1:], remaining_ranges[1:], 0)
        if not current_streak:
            # try continuing like it's .
            possibilities += recurse(remaining_string[1:], remaining_ranges, 0)
        # try continuing like it's #
        possibilities += recurse(remaining_string[1:], remaining_ranges, current_streak+1)
    return possibilities

records = []
with open("input.txt") as f:
    for line in f:
        record_line,ranges = line.strip().split(" ")
        ranges = [int(c) for c in ranges.split(",")]
        # part 2
        record_line = "?".join([record_line]*5)
        ranges = ranges*5
        records.append(Record(record_line,ranges))

arrangements = []
for record in records:
    if not record.more_damaged:
        arrangements.append(1)
    else:
        combos = recurse(record.line, tuple(record.ranges), 0)
        if combos == 0:
            print(combos, record)
        arrangements.append(combos)

print(sum(arrangements))