import math

grid = []
operators = []
with open("input_6.txt") as f:
    for line in f:
        l = [c for c in line if c != "\n"]
        grid.append(l)

operators = grid.pop()
context = ""
part2 = 0
current_problem = []
for idx,o in enumerate(operators):
    if o in ["+","*"]:
        if context == "+":
            part2 += sum(current_problem)
        elif context == "*":
            part2 += math.prod(current_problem)
        context = o
        current_problem = []
    
    num = []
    for row in range(len(grid)):
        if grid[row][idx].isdigit():
            num.append(grid[row][idx])
    if num:
        current_problem.append(int("".join(num)))

if context == "+":
    part2 += sum(current_problem)
elif context == "*":
    part2 += math.prod(current_problem)
print("Part 2", part2)