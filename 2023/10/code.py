# 7086
# 317

lines = []
with open("input.txt") as f:
    for line in f:
        lines.append([c for c in line.strip()])

for y,col in enumerate(lines):
    for x,row in enumerate(col):
        if lines[y][x] == "S":
            start = (x,y)
            break

ans = 1

position = [start[0], start[1]-1]
last_move = [0, -1]
while lines[position[1]][position[0]] != 'S':
    tile = lines[position[1]][position[0]]
    match tile:
        case "|":
            if last_move == [0, 1]:
                position[1] += 1
            elif last_move == [0, -1]:
                position[1] -= 1
        case "-":
            if last_move == [1, 0]:
                position[0] += 1
            elif last_move == [-1, 0]:
                position[0] -= 1
        case "7":
            if last_move == [1, 0]:
                position[1] += 1
                last_move = [0, 1]
            elif last_move == [0, -1]:
                position[0] -= 1
                last_move = [-1, 0]
        case "J":
            if last_move == [1, 0]:
                position[1] -= 1
                last_move = [0, -1]
            elif last_move == [0, 1]:
                position[0] -= 1
                last_move = [-1, 0]
        case "L":
            if last_move == [-1, 0]:
                position[1] -= 1
                last_move = [0, -1]
            elif last_move == [0, 1]:
                position[0] += 1
                last_move = [1, 0]
        case "F":
            if last_move == [-1, 0]:
                position[1] += 1
                last_move = [0, 1]
            elif last_move == [0, -1]:
                position[0] += 1
                last_move = [1, 0]
        case ".":
            break
        
    ans += 1
        
print(ans//2)

array = ["|", "J", "L", "S"]

for y in lines:
    y.append(".")

def chars_left(x,y):
  count = 0
  for idx in range(x):
    if lines[y][idx] in array:
      count += 1
  return count 

part2 = 0
for y,_ in enumerate(lines):
  for x,_ in enumerate(lines[0]):
    if lines[y][x] == ".":
      chars = chars_left(x,y)
      if chars % 2 == 1:
        part2 += 1

print(part2)