from dataclasses import dataclass
import math

@dataclass
class Node:
    id: str
    left: str
    right: str

all_input = []
with open("input.txt") as f:
    for line in f:
        all_input.append(line.strip())

instructions = all_input[0]
node_input = all_input[2:]
nodes = {}
for line in node_input:
    id,children = line.split("=")
    id = id.strip()
    left = children.strip()[1:4]
    right = children.strip()[6:9]
    node = Node(id,left,right)
    nodes[id] = node

print(nodes)

starts = [nodes["AAA"], nodes["LQA"], nodes["SGA"], nodes["BJA"], nodes["SVA"], nodes["GFA"]]
finishes = [nodes["ZZZ"], nodes["QNZ"], nodes["LHZ"], nodes["QXZ"], nodes["FBZ"], nodes["BRZ"]]

current_node = starts

steps_record = []
for start in starts:
    current_node = start
    inst_idx = 0
    steps = 0
    while current_node not in finishes:
        inst = instructions[inst_idx]
        if inst == "L":
            current_node = nodes[current_node.left]
        if inst == "R":
            current_node = nodes[current_node.right]
        steps += 1
        inst_idx += 1
        if inst_idx >= len(instructions):
            inst_idx = 0

    steps_record.append(steps)

print(math.lcm(*steps_record))