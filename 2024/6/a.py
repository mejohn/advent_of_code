from copy import deepcopy
from dataclasses import dataclass
from itertools import combinations

@dataclass 
class Point:
    x: int
    y: int
    id: int
    char: str

    def __hash__(self):
        return hash(id)



@dataclass
class Grid:
    points: dict[int, Point]
    max_x: int
    max_y: int

    def get_row(self, node):
        return dict(sorted({id: n for id,n in self.points.items() if node.y == n.y}.items(), key=lambda n: n[1].x))
    
    def get_column(self, node):
        return dict(sorted({id: n for id,n in self.points.items() if node.x == n.x}.items(), key=lambda n: n[1].y))
    
points = {}
with open("input.txt") as f:
    for y,line in enumerate(f):
        for x,char in enumerate(line.strip()):
            points[f"{x}.{y}"] = Point(x,y,f"{x}.{y}", char)
            if char == "^":
                guard = points[f"{x}.{y}"]

grid = Grid(points, x, y)

dirs = {
    "^": (0,-1),
    ">": (1,0),
    "v": (0,1),
    "<": (-1,-0)
}
rot = {
    "^": ">",
    ">": "v",
    "v": "<",
    "<": "^"
}

original_guard = guard.id
original_points = deepcopy(points)
will_loop = set()
for point in original_points.values():
    if point.char != "^" and point.char != "#":
        points = {id:point for id,point in original_points.items()}
        guard = points[original_guard]
        guard.char = "^"
        visited = {(guard.x, guard.y, guard.char)}
        points[point.id].char = "O"
        while guard is not None:
            dir = guard.char
            delta = dirs[dir]
            next_id = f"{guard.x+delta[0]}.{guard.y+delta[1]}"
            if next_id not in points: 
                guard = None
                break
            if points[next_id].char == "#" or points[next_id].char == "O":
                guard.char = rot[guard.char]
            else:
                guard.char = "."
                guard = points[next_id]
                guard.char = dir
                if (guard.x, guard.y, guard.char) in visited:
                    print(visited)
                    will_loop.add(point.id)
                    guard = None
                    break
                visited.add((guard.x, guard.y, guard.char))


print(will_loop)
print(len(will_loop))