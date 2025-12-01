from itertools import combinations
from collections import defaultdict

rows = []
with open("input.txt") as f:
    for line in f:
        rows.append([c for c in line.strip()])

nodes = defaultdict(list)
for i,row in enumerate(rows):
    for j,col in enumerate(row):
        if col != '.':
            nodes[col].append((j,i))

print(nodes)
antinodes = defaultdict(set)
unis = set()
for char,points in nodes.items():
    pairs = combinations(points, 2)
    for n1,n2 in pairs:
        dx = n2[0] - n1[0]
        dy = n2[1] - n1[1]
        print(n1, n2, dx, dy)
        x = n2[0]+dx
        y = n2[1]+dy
        print(x,y, x in range(0, len(rows[0])), y in range(0, len(rows)))
        unis.update([n2, n1])
        while x in range(0, len(rows[0])) and y in range(0, len(rows)):
#         if dx+n2[0] in range(0, len(rows[0])) and dy+n2[1] in range(0, len(rows)):
            print("antinode n2", x,y)
            unis.add((x, y))
            x = x+dx
            y = y+dy
        dx *= -1
        dy *= -1
        x = n1[0]+dx
        y = n1[1]+dy
        print(x,y, x in range(0, len(rows[0])), y in range(0, len(rows)), len(rows[0]), len(rows))
        while x in range(0, len(rows[0])) and y in range(0, len(rows)):
#        if dx+n1[0] in range(0, len(rows[0])) and dy+n1[1] in range(0, len(rows)):
            print("antinode n1", x,y)
            unis.add((x, y))
            x = x+dx
            y = y+dy

print(antinodes)

test = [(6, 0), (11, 0), (3,1), (4,2), (10,2),(2,3),(9,4),(1,5),(3,6), (0,7), (7,7), (10,10), (10,11), (6,5)]

sum = 0
for char,a_list in antinodes.items():
    sum += len(set(a_list))
print(sum)

print(len(unis))