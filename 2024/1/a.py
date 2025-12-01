from collections import Counter


left = []
right = []
with open("input.txt") as f:
    for line in f:
        l, r = line.split("   ")
        left.append(int(l.strip()))
        right.append(int(r.strip()))

left = sorted(left)
right = sorted(right)

distances = []
for i in range(0, len(left)):
    distances.append(abs(left[i] - right[i]))

print(sum(distances))

counter = Counter()
for r in right:
    if r in left:
        counter[r] += 1

print(counter)

sum = 0
for l in left:
    if l in counter:
        sum+= counter[l] * l

print(sum)