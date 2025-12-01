from dataclasses import dataclass
from enum import Enum
import sys

sys.setrecursionlimit(500000)

class Dir(Enum):
    NORTH = (0,1)
    EAST = (1,0)
    SOUTH = (0,-1)
    WEST = (-1,0)

@dataclass 
class Point:
    x: int
    y: int
    id: int
    symbol: str
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
    
    def get_energized(self):
        return [id for id,point in self.points.items() if point.energized]
    
    def reset(self):
        for point in self.points:
            self.points[point].energized = False
    
    def traverse_beam(self, location, dir, traversed):
        x = location[0] + dir.value[0]
        y = location[1] + dir.value[1]
        if x < 0 or x >= self.max_x or y < 0 or y >= self.max_y or (x,y,dir) in traversed:
            return
        n = self.points[(x,y)]
        self.points[(x,y)].energized = True
        traversed.append((x,y,dir))
        match n.symbol:
            case "/":
                if dir == Dir.NORTH:
                    self.traverse_beam((x,y),Dir.WEST,traversed)
                if dir == Dir.WEST:
                    self.traverse_beam((x,y),Dir.NORTH,traversed)
                if dir == Dir.SOUTH:
                    self.traverse_beam((x,y),Dir.EAST,traversed)
                if dir == Dir.EAST:
                    self.traverse_beam((x,y),Dir.SOUTH,traversed)
            case "a":
                if dir == Dir.NORTH:
                    self.traverse_beam((x,y),Dir.EAST,traversed)
                if dir == Dir.EAST:
                    self.traverse_beam((x,y),Dir.NORTH,traversed)
                if dir == Dir.SOUTH:
                    self.traverse_beam((x,y),Dir.WEST,traversed)
                if dir == Dir.WEST:
                    self.traverse_beam((x,y),Dir.SOUTH,traversed)
            case "-":
                if dir in [Dir.NORTH, Dir.SOUTH]:
                    self.traverse_beam((x,y),Dir.EAST,traversed)
                    self.traverse_beam((x,y),Dir.WEST,traversed)
                else:
                    self.traverse_beam((x,y),dir,traversed)

            case "|":
                if dir in [Dir.EAST, Dir.WEST]:
                    self.traverse_beam((x,y),Dir.NORTH,traversed)
                    self.traverse_beam((x,y),Dir.SOUTH,traversed)
                else:
                    self.traverse_beam((x,y),dir,traversed)
            case ".":
                self.traverse_beam((x,y),dir,traversed)
    
points = {}
with open("input.txt") as f:
    for y,line in enumerate(f):
        for x,char in enumerate(line.strip()):
            points[(x,y)] = Point(x,y,f"{x}.{y}", char if char != "\\" else "a", False)

grid = Grid(points, x+1, y+1)


traversed = [(0,0,Dir.NORTH)]
grid.traverse_beam((0,0),Dir.NORTH,traversed)

energized = grid.get_energized()

print("PART 1: ", len(energized)+1)
grid.reset()

energies = []
for y in range(grid.max_y):
    for x in (-1,grid.max_x):
        grid.traverse_beam((x,y),Dir.EAST,[])
        energies.append(len(grid.get_energized()))
        grid.reset()

for y in range(grid.max_x):
    for x in (-1,grid.max_y):
        grid.traverse_beam((x,y),Dir.SOUTH,[])
        energies.append(len(grid.get_energized()))
        grid.reset()

print("PART 2: ", max(energies))