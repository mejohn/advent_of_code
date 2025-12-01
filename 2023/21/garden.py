from collections import defaultdict
import numpy as np

directions = {
    "north": (0, 1), 
    "east": (1,0), 
    "south": (0, -1),
    "west": (-1, 0), 
}

with open("input.txt") as f:
    all_input = [line.strip() for line in f.readlines()]

grid = {}
for y, line in enumerate(all_input):
    for x, char in enumerate(line):
        grid[(x, y)] = char
        if char == 'S':
            start = (x, y)

max_x, max_y = x+1, y+1

steps = 64
can_reach = defaultdict(set)
can_reach[0].add(start)
for step in range(steps):
    for point in can_reach[step]:
        x, y = point
        for dir in directions.values():
            dx, dy = dir
            new_x, new_y = x + dx, y + dy
            if (new_x,new_y) in grid and grid[(new_x,new_y)] in ['.', 'S']:
                print(step+1, new_x, new_y, grid[(new_x,new_y)])
                can_reach[step+1].add((new_x, new_y))

print(len(can_reach[steps]))

steps2 = 26501365 - 1
# no more brute forcing :'(
# lengths = []
# for step in range(steps, steps2):
#     for point in can_reach[step]:
#         x, y = point
#         for dir in directions.values():
#             dx, dy = dir
#             new_x, new_y = x + dx, y + dy
#             grid_x,grid_y = new_x % max_x, new_y % max_y
#             print(new_x, new_y, grid_x, grid_y)
#             if (grid_x,grid_y) in grid and grid[(grid_x,grid_y)] in ['.', 'S']:
#                 print(step+1, new_x, new_y, grid[(grid_x,grid_y)])
#                 can_reach[step+1].add((new_x, new_y))
# print(len(can_reach[steps2]))

print(max_x, max_y, start)
# grid is a square, start is in the middle. 

# regression?
test_steps = [6, 10, 50, 100, 500, 1000] 
test_x = 5000
test_reached = [16, 50, 1594, 6536, 167004, 668697] # 16733044
test_y = 16733044

model_2 = np.poly1d(np.polyfit(test_steps, test_reached, 2))
print(model_2)
guess_check = (model_2[0]*(test_x**2)) + (model_2[1]*test_x) + (model_2[2])
print(test_y, guess_check)

import ipdb; ipdb.set_trace()


regression_check = [(step,len(can_reach[step])) for step in range(len(can_reach))]
print(regression_check)

x_list = list(range(len(can_reach)))
y_list = [len(can_reach[step]) for step in x_list]

model_2 = np.poly1d(np.polyfit(x_list, y_list, 2))
model_3 = np.poly1d(np.polyfit(x_list, y_list, 3))

guess_2 = (model_2[0]*(steps2**2)) + (model_2[1]*steps2) + (model_2[2])
guess_3 = (model_3[0]*(steps2**3)) + (model_3[1]*(steps2**2) + (model_3[2]*steps2) + model_3[3])

print(guess_2) # 5501395576229507, 5501395161051236
print(guess_3) # -8.686033846875158e+22, -8.686032863601246e+22
