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

dirs = [[(2,0), [(1,1),(1,-1)], [(0,2),(2,2)]],
        [(0,2),[(1,1),(-1,1)], [(2,2),(2,0)]],
        [(-2,0),[(-1,-1),(-1,1)]],
        [(0,-2),[(1,-1),(-1,-1)]]
        ]

dirs = [
    [(2,0), (1,1), [(0,2),(2,2)]],
    [(2,0), (1,-1), [(0,2),(2,-2)]],
    [(0,2), (1,1), [(2,2),(2,0)]],
    [(0,2), (-1,1), [(2,0), (-2,2)]],
    [(-2,0), (-1,-1), [(0,-2), (-2,-2)]],
    [(-2,0), (-1,1), [(0,-2), (-2,2)]],
    [(0,-2), (1,-1), [(-2,0),(2,-2)]],
    [(0,-2), (-1,-1), [(-2,0),(-2,-2)]],
]

points = {}
with open("input.txt") as f:
    for y,line in enumerate(f):
        for x,char in enumerate(line.strip()):
            points[f"{x}.{y}"] = Point(x,y,f"{x}.{y}", char)

grid = Grid(points, x, y)
# print(points)

count = 0
for id,point in points.items():
    if point.char == "M":
        for m_dir,a_dir,s_dirs in dirs:
            m_id = f"{point.x+m_dir[0]}.{point.y+m_dir[1]}"
            if m_id in points and points[m_id].char == "M":
                a_id = f"{point.x+a_dir[0]}.{point.y+a_dir[1]}"
                if a_id in points and points[a_id].char == "A":
                    s_id1 = f"{point.x+s_dirs[0][0]}.{point.y+s_dirs[0][1]}"
                    s_id2 = f"{point.x+s_dirs[1][0]}.{point.y+s_dirs[1][1]}"
                    if s_id1 in points and s_id2 in points and points[s_id1].char == "S" and points[s_id2].char == "S":
                        count += 1


print(count)