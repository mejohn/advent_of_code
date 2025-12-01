
"""
% flip flop, start off
    ignore high pulse
    for low pulse
        if off, toggle and send high
        if on, toggle and send low
& conjunction, remember last for all inputs, start low
    update memory
    if all inputs high, send low
    otherwise send high
broadcast
    sends received pulse to all children
button
    sends single low pulse to broadcaster

pulses processed in order of sending -> queue?

low signal = True
high signal = False
"""
from __future__ import annotations
from dataclasses import dataclass
from collections import deque
import math

@dataclass
class Node:
    name: str

    def send_signal(self, parent, received):
        return True


@dataclass
class FlipFlop(Node):
    toggle: bool = False

    def send_signal(self, parent, received):
        if received:
            current = self.toggle
            self.toggle = not self.toggle
            if current:
                return True
            return False
        return None

@dataclass
class Conjunction(Node):
    signals: dict[str, bool]

    def send_signal(self, parent, received):
        self.signals[parent.name] = received
        if all([not val for val in self.signals.values()]):
            return True
        return False
    

all_input = []
with open("input.txt") as f:
    for line in f:
        all_input.append(line.strip())

children = {}
nodes = {}
for line in all_input:
    name,others = line.split("->")
    match line[0]:
        case "%":
            node = FlipFlop(
                name=name[1:].strip(),
            )
            nodes[node.name] = node
            children[node.name] = [n.strip() for n in others.split(",")]
        case "&":
            node = Conjunction(
                name=name[1:].strip(),
                signals=[]
            )
            nodes[node.name] = node
            children[node.name] = [n.strip() for n in others.split(",")]
        case "b":
            broadcaster = Node(
                name="broadcaster",
            )
            nodes["broadcaster"] = broadcaster
            children["broadcaster"] = [n.strip() for n in others.split(",")]

parents = {}
for node,childs in children.items():
    for child in childs:
        if child not in parents:
            parents[child] = [node]
        else:
            parents[child].append(node)

for name,node in nodes.items():
    if isinstance(node,Conjunction):
        node.signals = {c:True for c in parents[name]}

print("NODES: ", nodes)
print("CHILDREN: ", children)
print("PARENTS", parents)

def flopped(nodes):
    return all([not f.toggle for f in nodes.values() if isinstance(f, FlipFlop)])

def process_signal(signals, low, high,lb_parents):
    node,parent,signal = signals[0]
    onward_signal = node.send_signal(parent, signal)
    nodes[node.name] = node
    lb_out = []
    if onward_signal is not None:
        if onward_signal:
            low += len(children[node.name])
        else:
            high += len(children[node.name])
        for child in children[node.name]:
            if child in nodes:
                signals.append([nodes[child], node, onward_signal])
                if child == "lb" and not onward_signal:
                    lb_out.append(node.name)
            # elif child == "rx":
            #     return low,high,True,None
    signals.popleft()
    return low,high,False,lb_out

cycle = 1
signals = deque([[nodes["broadcaster"], "button", None]])

low = 0
high = 0
rx = False
# lb needs a high pulse from all of these at the same time
# to turn on rx
lb_parents = {"rz":0, "lf":0, "br":0, "fk":0}
lb_needed = list(lb_parents.keys())
while not rx: # cycle < 1000: 
    while signals:
        low,high,rx,lb_vals = process_signal(signals, low, high,lb_parents.keys())
        if lb_vals:
            print(lb_vals, cycle)
            for parent,val in lb_parents.items():
                if val == 0 and parent in lb_vals:
                    lb_parents[parent] = cycle
                    lb_needed.remove(parent)
        if not lb_needed:
            break

    cycle += 1
    # print(cycle, lb_parents)
    
    if not lb_needed:
        break
    
    if flopped(nodes):
        print(cycle)
        print("LOW: ", low)
        print("HIGH: ", high)
        break
    else:
        signals = deque([[nodes["broadcaster"], "button", None]])
        low += 1

# cycles = 1000 / cycle
# print(cycles)
# print(low*cycles)
# print(high*cycles)

# print((low*cycles)*(high*cycles))
print(cycle)
print(low*high)
print(math.lcm(*list(lb_parents.values())))
