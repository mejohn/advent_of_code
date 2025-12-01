from dataclasses import dataclass
from itertools import combinations

@dataclass 
class Point:
    x: int
    y: int
    id: int
    galaxy: bool

@dataclass
class Grid:
    points: dict[int, Point]
    max_x: int
    max_y: int

    def get_row(self, node):
        return dict(sorted({id: n for id,n in self.points.items() if node.y == n.y}.items(), key=lambda n: n[1].x))
    
    def get_column(self, node):
        return dict(sorted({id: n for id,n in self.points.items() if node.x == n.x}.items(), key=lambda n: n[1].y))

    def get_empty_rows(self):
        empties = []
        for row in range(self.max_y+1):
            if all([not point.galaxy for point in self.points.values() if point.y == row]):
                empties.append(row)
        return empties
    
    def get_empty_columns(self):
        empties = []
        for col in range(self.max_x+1):
            if all([not point.galaxy for point in self.points.values() if point.x == col]):
                empties.append(col)
        return empties

    def get_galaxies(self):
        return {point.id: point for point in self.points.values() if point.galaxy}
    
    def shortest_path(self, galaxy1, galaxy2, empty_rows, empty_columns, offset):
        x1, x2 = min(galaxy1.x, galaxy2.x), max(galaxy1.x, galaxy2.x)
        y1, y2 = min(galaxy1.y, galaxy2.y), max(galaxy1.y, galaxy2.y)
        x, y = x2 - x1, y2 - y1
        print("initial", x, y)
        for row in empty_rows:
            if row in range(y1, y2):
                x += offset - 1
                print("row", row, x1, x2, x, y)
        for col in empty_columns:
            if col in range(x1, x2):
                y += offset - 1
                print("col", col, y1, y2, x, y)
        print("after", x, y)
        return x + y 

points = {}
with open("input.txt") as f:
    for y,line in enumerate(f):
        for x,char in enumerate(line.strip()):
            points[f"{x}.{y}"] = Point(x,y,f"{x}.{y}", True if char == "#" else False)

grid = Grid(points, x, y)
print(x, y)
empty_rows = grid.get_empty_rows()
empty_columns = grid.get_empty_columns()

print(empty_columns)
print(empty_rows)

galaxies = grid.get_galaxies()
combos = list(combinations(galaxies, 2))

dists = []
for galaxy1,galaxy2 in combos:
    print(galaxy1, galaxy2)
    distance = grid.shortest_path(grid.points[galaxy1], grid.points[galaxy2], empty_rows, empty_columns, 1000000)
    print(distance)
    dists.append(distance)

print(len(combos))
print(dists)
print(sum(dists))

