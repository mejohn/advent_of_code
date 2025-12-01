import re

lines = []
with open("input.txt") as f:
    for line in f:
        lines.append(line.strip())

line = "".join(lines)
pairs = []
regex = r"mul\(\d+\,\d+\)"
pattern = re.compile(regex)

for match in pattern.findall(line):
    p1,p2 = match[4:-1].split(",")
    pairs.append(int(p1)*int(p2))

print(sum(pairs))