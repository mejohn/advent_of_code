from dataclasses import dataclass

@dataclass 
class Point:
    x: int
    y: int
    id: int
    symbol: str

@dataclass
class Grid:
    points: dict[int, Point]
    max_x: int
    max_y: int

    def get_row(self, idx):
        return dict(sorted({id: n for id,n in self.points.items() if idx == n.y}.items(), key=lambda n: n[1].x))
    
    def get_column(self, idx):
        return dict(sorted({id: n for id,n in self.points.items() if idx == n.x}.items(), key=lambda n: n[1].y))
    
    def get_rolling_rocks_row(self,y):
        row = self.get_row(y).values()
        return [(n.x, n.y) for n in row if n.symbol == "O"]
    
    def get_rolling_rocks_col(self, x):
        row = self.get_col(x).values()
        return [(n.x, n.y) for n in row if n.symbol == "O"]
    
    def get_rows(self):
        return [self.get_row(idx).values() for idx in range(self.max_y)]
    
    def get_symbols(self):
        return [n.symbol for row in self.get_rows() for n in row]
    
    def calculate_load(self):
        previous_row = self.get_rolling_rocks_row(0)
        load = len(previous_row)*self.max_y
        print(load)
        for idx in range(1,self.max_y):
            current_row = self.get_rolling_rocks_row(idx)
            load += len(current_row)*(self.max_y-idx)
        return load

def tilt_one_north(grid):
    previous_row = grid.get_row(0)
    new_points = {id:n for id,n in grid.points.items()}
    for idx in range(1, grid.max_y):
        current_row = grid.get_row(idx)
        for id,node in current_row.items():
            if node.symbol == "O":
                new_id = f"{node.x}.{node.y-1}"
                if previous_row[new_id].symbol == ".":
                    new_points[new_id] = Point(node.x, node.y-1, new_id, node.symbol)
                    new_points[node.id] = Point(node.x, node.y, id, ".")
                    current_row[node.id] = Point(node.x, node.y, id, ".")
        previous_row = current_row
    return Grid(new_points, grid.max_x, grid.max_y)

def tilt_one_south(grid):
    previous_row = grid.get_row(grid.max_y-1)
    new_points = {id:n for id,n in grid.points.items()}
    for idx in range(2, grid.max_y):
        current_row = grid.get_row(grid.max_y - idx)
        for id,node in current_row.items():
            if node.symbol == "O":
                new_id = f"{node.x}.{node.y+1}"
                if previous_row[new_id].symbol == ".":
                    new_points[new_id] = Point(node.x, node.y+1, new_id, node.symbol)
                    new_points[node.id] = Point(node.x, node.y, id, ".")
                    current_row[node.id] = Point(node.x, node.y, id, ".")
        previous_row = current_row
    return Grid(new_points, grid.max_x, grid.max_y)

def tilt_one_west(grid):
    previous_row = grid.get_column(0)
    new_points = {id:n for id,n in grid.points.items()}
    for idx in range(1, grid.max_x):
        current_row = grid.get_column(idx)
        for id,node in current_row.items():
            if node.symbol == "O":
                new_id = f"{node.x-1}.{node.y}"
                if previous_row[new_id].symbol == ".":
                    new_points[new_id] = Point(node.x-1, node.y, new_id, node.symbol)
                    new_points[node.id] = Point(node.x, node.y, id, ".")
                    current_row[node.id] = Point(node.x, node.y, id, ".")
        previous_row = current_row
    return Grid(new_points, grid.max_x, grid.max_y)

def tilt_one_east(grid):
    previous_row = grid.get_column(grid.max_x-1)
    new_points = {id:n for id,n in grid.points.items()}
    for idx in range(2, grid.max_x):
        current_row = grid.get_column(grid.max_x - idx)
        for id,node in current_row.items():
            if node.symbol == "O":
                new_id = f"{node.x+1}.{node.y}"
                if previous_row[new_id].symbol == ".":
                    new_points[new_id] = Point(node.x+1, node.y, new_id, node.symbol)
                    new_points[node.id] = Point(node.x, node.y, id, ".")
                    current_row[node.id] = Point(node.x, node.y, id, ".")
        previous_row = current_row
    return Grid(new_points, grid.max_x, grid.max_y)

def tilt(grid, direction):
    match direction:
        case "north":
            north_grid = tilt_one_north(grid)
            next_grid = tilt_one_north(north_grid)
            while north_grid.get_symbols() != next_grid.get_symbols():
                north_grid = tilt_one_north(next_grid)
                next_grid = tilt_one_north(north_grid)
            return north_grid
        case "west":
            north_grid = tilt_one_west(grid)
            next_grid = tilt_one_west(north_grid)
            while north_grid.get_symbols() != next_grid.get_symbols():
                north_grid = tilt_one_west(next_grid)
                next_grid = tilt_one_west(north_grid)
            return north_grid
        case "south":
            north_grid = tilt_one_south(grid)
            next_grid = tilt_one_south(north_grid)
            while north_grid.get_symbols() != next_grid.get_symbols():
                north_grid = tilt_one_south(next_grid)
                next_grid = tilt_one_south(north_grid)
            return north_grid
        case "east":
            north_grid = tilt_one_east(grid)
            next_grid = tilt_one_east(north_grid)
            while north_grid.get_symbols() != next_grid.get_symbols():
                north_grid = tilt_one_east(next_grid)
                next_grid = tilt_one_east(north_grid)
            return north_grid
def spin(grid):
    directions = ["north", "west", "south", "east"]
    for direction in directions:
        grid = tilt(grid, direction)
    return grid

points = {}
with open("test.txt") as f:
    for y,line in enumerate(f):
        for x,char in enumerate(line.strip()):
            points[f"{x}.{y}"] = Point(x,y,f"{x}.{y}", char)

grid = Grid(points, x+1, y+1)

# north_grid = tilt_north(grid)
# print(north_grid.points)
# print("".join(north_grid.get_symbols()))
# print(north_grid.calculate_load())

cycles = 1000000000
grids = []
cached = False
index = 0

for cycle in range(cycles):
    print(cycle)
    if cached:
        print("CYCLING CACHED", len(grids))
        grid = grids[offset+index]
        index += 1
        if index > len(grids):
            index = 0
    if not cached:
        grid = spin(grid)
        if grids and grid == grids[0]:
            cached = True
            offset = cycles%cycle
        else:
            grids.append(grid)

print(grid.calculate_load())