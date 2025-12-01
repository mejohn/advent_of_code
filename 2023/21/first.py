from dataclasses import dataclass
from enum import Enum
import sys

sys.setrecursionlimit(500000)

class Dir(Enum):
    NORTH = (0,-1)
    EAST = (1,0)
    SOUTH = (0,1)
    WEST = (-1,0)

@dataclass 
class Point:
    x: int
    y: int
    garden: bool
    could_reach: bool

    @property
    def symbol(self):
        if self.could_reach:
            return "O"
        return "." if self.garden else "#"

@dataclass
class Grid:
    points: dict[int, Point]
    max_x: int
    max_y: int

    def get_row(self, idx):
        return dict(sorted({id: n for id,n in self.points.items() if idx == n.y}.items(), key=lambda n: n[1].x))
    
    def get_rows(self):
        return [self.get_row(idx).values() for idx in range(self.max_y)]
    
    def get_symbols(self):
        out = []
        for row in self.get_rows():
            out.append("".join([n.symbol for n in row]))
        return out
    
    
    def get_around(self, node):
       return {
            Dir.NORTH: (node.x+Dir.NORTH.value[0],node.y+Dir.NORTH.value[1]),
            Dir.EAST: (node.x+Dir.EAST.value[0],node.y+Dir.EAST.value[1]),
            Dir.SOUTH: (node.x+Dir.SOUTH.value[0],node.y+Dir.SOUTH.value[1]),
            Dir.WEST: (node.x+Dir.WEST.value[0],node.y+Dir.WEST.value[1]),

        }
    
    def get_could_reach(self):
        return [id for id,point in self.points.items() if point.could_reach]
    
    def reset(self):
        for point in self.points:
            self.points[point].energized = False

    def walk_garden(self, location, dir, traversed, steps):
        x = location[0] + dir.value[0]
        y = location[1] + dir.value[1]
        if x < 0 or x >= self.max_x or y < 0 or y >= self.max_y or (x,y,dir) in traversed:
            return
        n = self.points[(x,y)]
        traversed.append((x,y,dir))
        print(steps, (x,y))
        self.points[(x,y)].could_reach = True
        if steps == 6:
            return
        around = self.get_around(n)
        for next_dir,point in around.items():
            if point in self.points and self.points[point].garden:
                self.walk_garden(point, next_dir, traversed, steps+1)

points = {}
with open("test.txt") as f:
    for y,line in enumerate(f):
        for x,char in enumerate(line.strip()):
            points[(x,y)] = Point(x,y, True if char in [".", "S"] else False, False)
            if char == "S":
                start_x,start_y = x,y

grid = Grid(points, x+1, y+1)

traversed = []
steps = 0

grid.points[(start_x,start_y)].could_reach = True
around_start = grid.get_around(grid.points[(start_x,start_y)])
for next_dir,point in around_start.items():
    if point in grid.points and grid.points[point].garden:
        grid.walk_garden(point, next_dir, traversed, steps+1)

could_reach = grid.get_could_reach()

print(could_reach)
print(len(could_reach))

for row in grid.get_symbols():
    print(row)