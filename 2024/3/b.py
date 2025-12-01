import re

lines = []
with open("input.txt") as f:
    for line in f:
        lines.append(line.strip())

line = "".join(lines)
pairs = []
regex_do = r"do\(\)"
regex_mul = r"mul\(\d+\,\d+\)"
regex_dont = r"don\'t\(\)"
pattern_do = re.compile(regex_do)
pattern_mul = re.compile(regex_mul)
pattern_dont = re.compile(regex_dont)

dont_matches = [m.start(0)for m in re.finditer(pattern_dont, line)]
do_matches = [m.start(0) for m in re.finditer(pattern_do, line)]
do = True
for idx in range(len(line)):
    if idx in do_matches:
        do = True
    if idx in dont_matches:
        do = False
    if do:
        if match:=pattern_mul.match(line[idx:]):
            print(match)
            p1,p2 = match.group(0)[4:-1].split(",")
            pairs.append(int(p1)*int(p2))

print(pairs)
print(sum(pairs))