from dataclasses import dataclass
from itertools import combinations

@dataclass 
class Point:
    x: int
    y: int
    id: int
    char: str

@dataclass
class Grid:
    points: dict[int, Point]
    max_x: int
    max_y: int

    def get_row(self, node):
        return dict(sorted({id: n for id,n in self.points.items() if node.y == n.y}.items(), key=lambda n: n[1].x))
    
    def get_column(self, node):
        return dict(sorted({id: n for id,n in self.points.items() if node.x == n.x}.items(), key=lambda n: n[1].y))

# lines = []
# with open("test.txt") as f:
#     for line in f:
#         lines.append(line.strip())

# print(lines)

dirs = [(0,1),(1,0),(0,-1),(-1,0),(1,1),(-1,-1),(-1,1),(1,-1)]
points = {}
with open("input.txt") as f:
    for y,line in enumerate(f):
        for x,char in enumerate(line.strip()):
            points[f"{x}.{y}"] = Point(x,y,f"{x}.{y}", char)

grid = Grid(points, x, y)
# print(points)

count = 0
for id,point in points.items():
    if point.char == "X":
        for dx,dy in dirs:
            m_id = f"{point.x+dx}.{point.y+dy}"
            if m_id in points and points[m_id].char == "M":
                a_id = f"{points[m_id].x+dx}.{points[m_id].y+dy}"
                if a_id in points and points[a_id].char == "A":
                    s_id = f"{points[a_id].x+dx}.{points[a_id].y+dy}"
                    if s_id in points and points[s_id].char == "S":
                        count += 1

print(count)