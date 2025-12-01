from dataclasses import dataclass
from enum import Enum
import sys

sys.setrecursionlimit(500000)

class Dir(Enum):
    RIGHT = (1,0)
    DOWN = (0,1)
    LEFT= (-1,0)

@dataclass 
class Point:
    x: int
    y: int
    id: str
    heat_loss: int
    energized: bool

@dataclass
class Grid:
    points: dict[int, Point]
    max_x: int
    max_y: int

    def get_row(self, idx):
        return dict(sorted({id: n for id,n in self.points.items() if idx == n.y}.items(), key=lambda n: n[1].x))
    
    def get_column(self, idx):
        return dict(sorted({id: n for id,n in self.points.items() if idx == n.x}.items(), key=lambda n: n[1].y))

    def reset(self):
        for point in self.points:
            self.points[point].energized = False

    def traverse(self, location, dir, traversed, heat_loss, minimum,streak):
        x = location[0] + dir.value[0]
        y = location[1] + dir.value[1]
        if x == self.max_x - 1 and y == self.max_y -1:
            return sum(heat_loss) + self.points[(x,y)].heat_loss
        if x < 0 or x >= self.max_x or y < 0 or y >= self.max_y or (x,y,dir) in traversed:
            return 0
        n = self.points[(x,y)]
        self.points[(x,y)].energized = True
        traversed.append((x,y,dir))
        heat_loss.append(n.heat_loss)
        # print(x,y,dir,sum(heat_loss))
        if minimum and heat_loss > minimum:
            return 0
        if dir != Dir.RIGHT:
            self.traverse((x,y),Dir.LEFT,traversed,heat_loss,minimum,0)
        if dir != Dir.LEFT:
            self.traverse((x,y),Dir.RIGHT,traversed,heat_loss, minimum,0)
        if streak < 3:
            self.traverse((x,y), Dir.DOWN,traversed,heat_loss,minimum,streak+1)



points = {}
with open("test.txt") as f:
    for y,line in enumerate(f):
        for x,char in enumerate(line.strip()):
            points[(x,y)] = Point(x,y,f"{x}.{y}", int(char), False)

grid = Grid(points, x+1, y+1)

start = (0,0)
end = (x,y)

min_path = grid.traverse(start, Dir.RIGHT, [(0,0,Dir.RIGHT)], [grid.points[(0,0)].heat_loss],None,0)
print(min_path)
min_path = grid.traverse(start, Dir.DOWN, [(0,0,Dir.DOWN)], [grid.points[(0,0)].heat_loss],min_path,0)
print(min_path)