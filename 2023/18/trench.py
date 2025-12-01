from dataclasses import dataclass
from enum import Enum

class Dir(Enum):
    NORTH = (0,-1)
    EAST = (1,0)
    SOUTH = (0,1)
    WEST = (-1,0)

@dataclass
class DigPlan:
    dir: Dir
    length: int
    color: str

@dataclass 
class Point:
    x: int
    y: int
    color: str
    energized: bool

@dataclass
class Grid:
    points: dict[int, Point]
    max_x: int
    max_y: int
    min_x: int
    min_y: int

    def get_row(self, idx):
        return dict(sorted({id: n for id,n in self.points.items() if idx == n.y}.items(), key=lambda n: n[1].x))
    
    def get_column(self, idx):
        return dict(sorted({id: n for id,n in self.points.items() if idx == n.x}.items(), key=lambda n: n[1].y))
    
    def get_energized(self):
        return [id for id,point in self.points.items() if point.energized]
    
    def dig_trench(self):
        previous_row = self.get_row(min_y)
        for row_id in range(min_y+1,max_y):
            row = self.get_row(row_id)
            ranges = []
            left, right = None, None
            if len(row) == 2:
                ranges.append((list(row.values())[0].x, list(row.values())[1].x))
            else:
                print("previous", previous_row)
                print("current", row)
                for col_id in range(min_x,max_x+1):
                    print(col_id,row_id)
                    if (col_id,row_id) in row:
                        if not left and not (col_id+1,row_id) in row:
                            print("left", col_id)
                            left = col_id
                        elif left and not right:
                            print("right", col_id)
                            right = col_id
                    
                    if left and right:
                        ranges.append((left,right))
                        left, right = None, None

            print(ranges)
            for r in ranges:
                for x in range(r[0],r[1]):
                    print(x,row_id)
                    if (x,row_id-1) in previous_row:
                        self.points[(x,row_id)] = Point(x,row_id,"",True)

            previous_row = self.get_row(row_id)
        
    def print_grid(self):
        for row_id in range(min_y,max_y+1):
            rep = []
            for col_id in range(min_x,max_x+1):
                rep.append("#" if (col_id,row_id) in points else ".")
            print("".join(rep))

plans = []
with open("input.txt") as f:
    for line in f:
        dir_char,num,color = line.strip().split(" ")
        match dir_char:
            case "R":
                dir = Dir.EAST
            case "L":
                dir = Dir.WEST
            case "U":
                dir = Dir.NORTH
            case "D":
                dir = Dir.SOUTH
        plans.append(DigPlan(dir,int(num),color[1:-1]))

print(plans)
min_x,min_y = 0,0
max_x,max_y = 0,0
x,y = 0,0

points = {}
for plan in plans:
    for i in range(plan.length):
        print(dir)
        x += plan.dir.value[0]
        y += plan.dir.value[1]
        points[(x,y)] = Point(x,y,plan.color,True)
        if x > max_x:
            max_x = x
        if y > max_y:
            max_y = y
        if x < min_x:
            min_x = x
        if y < min_y:
            min_y = y

print(points)
grid = Grid(points,max_x,max_y,min_x,min_y)

grid.dig_trench()

grid.print_grid()

print(len(grid.get_energized()))