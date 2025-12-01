from itertools import pairwise

def shoelace(points):
	area = 0
	for (x1, y1), (x2, y2) in pairwise(points):
		area += (x2 + x1) * (y2 - y1)

	return abs(area) // 2

def picks_theorem(points, perimeter):
	area = shoelace(points)
	return int(area - perimeter / 2 + 1) + perimeter

directions = {
	"R": (0, 1), 
	"0": (0, 1),
	"D": (1, 0), 
	"1": (1, 0),
	"L": (0, -1), 
	"2": (0, -1),
	"U": (-1, 0),
	"3": (-1, 0)
}

points = []
perimeter = 0
x,y = 0,0

points2 = []
perimeter2 = 0
x2,y2 = 0,0

with open("input.txt") as f:
	for line in f:
		direction, length, color = line.strip().split(" ")
		length = int(length)
		color = color[1:-1]

		dx, dy = directions[direction]
		x += dx * length
		y += dy * length
		points.append((x, y))
		perimeter += length
		
		length2 = int(color[1:-1],16)
		dx2,dy2 = directions[color[-1]]
		x2 += dx2 * length2 
		y2 += dy2 * length2
		points2.append((x2, y2))
		perimeter2 += length2

		

area = picks_theorem(points, perimeter)
print("PART 1:", area)

area2 = picks_theorem(points2, perimeter2)
print("PART 2:", area2)
