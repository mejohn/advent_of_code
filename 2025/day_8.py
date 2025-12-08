from itertools import combinations
import math

max_connections = 1000
connections = 0
points = []

with open("input_8.txt") as f:
    for line in f:
        point = tuple([int(x) for x in line.strip().split(",")])
        points.append(point)

points = sorted(points, key=lambda k: (k[0], k[1], k[2]))

distances = []
pairs = combinations(points, 2)
for a,b in pairs:
    distance = math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2 + (a[2]-b[2])**2)
    distances.append(tuple([distance, a, b]))

distances = sorted(distances, key=lambda k: k[0])
circuits = [set([point]) for point in points]
for d,a,b in distances:
    found = set()
    num_circuits = len(circuits)
    to_remove = []
    for idx,c in enumerate(circuits):
        if a in c or b in c:
            found.update(c)
            found.update({a,b})
            to_remove.append(c)
    for old in to_remove:
        circuits.remove(old)
    circuits.append(found)

    if len(circuits) <= num_circuits:
        connections += 1
    if connections == max_connections: 
        circuits = sorted(circuits, key=lambda k: -len(k))
        print("Part 1", len(circuits[0])*len(circuits[1])*len(circuits[2]))
    if len(circuits) == 1:
        print("Part 2", a[0]*b[0])
        break        
