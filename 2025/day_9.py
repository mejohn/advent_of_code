from collections import defaultdict
from itertools import combinations, chain

def border_line(a, b):
    if a[0] == b[0]:
        if a[1] - b[1] > 0:
            return a[0]-1, set(range(b[1]+1, a[1]))
        else:
            return a[0]+1, set(range(a[1]+1, b[1]))
    elif a[1] == b[1]:
        if a[0] - b[0] > 0:
            return a[1]+1, set(range(b[0]+1, a[0]))
        else:
            return a[1]-1, set(range(a[0]+1, b[0]))
    
def rectangle(a, b):
    return range(min(a[0], b[0]), max(a[0], b[0])+1), range(min(a[1], b[1]), max(a[1], b[1])+1)

points = []

with open("input_9.txt") as f:
    for l in f:
        point = tuple([int(x) for x in l.strip().split(",")])
        points.append(point)

areas = []
pairs = combinations(points, 2)
for a,b in pairs:
    area = abs((abs(a[0])-abs(b[0])+1) * (abs(a[1])-abs(b[1])+1))
    areas.append(tuple([area, a, b, rectangle(a,b)]))

areas = sorted(areas, key=lambda k: -k[0])
print("Part 1", areas[0][0])

x_bounds = defaultdict(set)
p1 = points[0]
for p2 in chain(points[1:], [points[0]]):
    if p1[0] == p2[0]:
        x,y = border_line(p1, p2)
        x_bounds[x].update(y)
    if p1[1] == p2[1]:
        y,x = border_line(p1, p2)
        for key in x:
            x_bounds[key].add(y)
    p1 = p2

x_ranges = {}
for x,y_set in x_bounds.items():
    y_ranges = []
    while y_set:
        mini = min(y_set)
        maxi = mini
        y_set.remove(mini)
        while True:
            maxi = maxi + 1
            if maxi in y_set:
                y_set.remove(maxi)
            else:
                y_ranges.append(range(mini, maxi))
                break
    x_ranges[x] = y_ranges


for idx,(area,a,b,l) in enumerate(areas):
    valid = True

    xs_to_check = [x for x in l[0] if x in x_ranges]
    for x in xs_to_check:
        for y_range in x_ranges[x]:
            if len(range(max(y_range.start, l[1].start), min(y_range.stop, l[1].stop))):
                valid = False
                break
        if not valid:
            break

    if valid:
        print("Part 2", area, a, b)
        break
        