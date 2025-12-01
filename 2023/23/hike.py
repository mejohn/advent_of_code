import sys

sys.setrecursionlimit(100000)
# longest path
# map bounded on all four sides
# never step onto same tile twice
# must follow direction of travel for arrows
directions = {
    "N": (0,-1),
    "E": (1,0),
    "S": (0,1),
    "W": (-1,0)
}

def hike(x, y, traversed, grid, end):
    if (x,y) == end:
        return len(traversed) - 1
    
    possible_directions = []
    char = grid[y][x]
    match char:
        case ".":
            possible_directions = directions.values()
        case ">":
            possible_directions = [directions["E"]]
        case "v":
            possible_directions = [directions["S"]]

    steps = -1
    for dir in possible_directions:
        dx, dy = x + dir[0], y + dir[1]
        if (dx,dy) in traversed or grid[dy][dx] == "#":
            continue
        traversed.add((dx,dy))
        next_steps = hike(dx, dy, traversed, grid, end)
        if steps != next_steps and next_steps > steps:
            steps = next_steps
        traversed.remove((dx,dy))
    return steps

def hike_slopes(x, y, traversed, grid, end):
    if (x,y) == end:
        return len(traversed) - 1
    
    possible_directions = directions.values()

    steps = -1
    for dir in possible_directions:
        dx, dy = x + dir[0], y + dir[1]
        if (dx,dy) in traversed or grid[dy][dx] == "#":
            continue
        traversed.add((dx,dy))
        next_steps = hike_slopes(dx, dy, traversed, grid, end)
        if steps != next_steps and next_steps > steps:
            steps = next_steps
        traversed.remove((dx,dy))
    return steps

lines = []
with open("input.txt") as f:
    for y,line in enumerate(f):
        new_line = []
        for x,char in enumerate(line.strip()):
            new_line.append(char)
            if y == 1 and char == ".":
                start = (x,y)
        lines.append(new_line)

end = (x-1, y)
grid = lines
grid_max = (x, y)

part1 = hike(start[0],start[1], set(start), grid, end)
print("PART 1: ", part1)

part2 = hike_slopes(start[0],start[1],set(start), grid, end)
print("PART 2: ", part2)
