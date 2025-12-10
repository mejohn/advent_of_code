def press(state, button):
    return [not s if idx in button else s for idx,s in enumerate(state)]

def tree(target, buttons):
    min_presses = 0
    state_cache = {}
    for button in buttons:
        initial = press([False]*len(target), button)
        latest_min = climb(target,  buttons, min_presses, initial, 1, [button], state_cache)
        if latest_min and (not min_presses or latest_min < min_presses):
            min_presses = latest_min
    return min_presses

def climb(target, buttons, current_min, state, presses, hit, state_cache):
    if presses >= state_cache.get(tuple(state), 100):
        return 0
    if target == tuple(state):
        # print(hit, presses, current_min)
        return presses
    if current_min and presses >= current_min:
        return 0
    possibles = []
    for button in buttons:
        if button in hit:
            continue
        state_cache[tuple(state)] = min(state_cache.get(tuple(state), 100), presses)
        if p := climb(target, buttons, current_min, press(state, button), presses+1, [*hit, button], state_cache):
            possibles.append(p)
    if possibles:
        return min(possibles)

targets = {}
buttons = {}
joltages = {}

with open ("input_10.txt") as f:
    for idx,line in enumerate(f):
        parse = line.strip().split(" ")
        targets[idx] = tuple([c == "#" for c in parse[0] if c in [".", "#"]])
        joltages[idx] = [int(d) for d in parse[-1][1:-1].split(",") if d]
        buttons[idx] = []
        for button in parse[1:-1]:
            b = []
            st = button.strip("()")
            if "," in st:
                b.extend([int(x) for x in st.split(",")])
            else:
                b.append(int(st))
            buttons[idx].append(tuple(b))

min_presses = {}
for idx, target in targets.items():
    print("\n\n", idx, target, buttons[idx], joltages[idx])
    min_presses[idx] = tree(target, buttons[idx])

print(min_presses)
print("Part 1", sum(min_presses.values()))
