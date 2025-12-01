from copy import deepcopy

all_input = []
with open("input.txt") as f:
    for line in f:
        all_input.append(line.strip())

rules_input = all_input[:508]
parts_input = all_input[509:]

print(rules_input[-1])
print(parts_input[0], parts_input[-1])

parts = []
for part in parts_input:
    x,m,a,s = part[1:-1].split(",")
    parts.append({
        "x": int(x.split("=")[1]),
        "m": int(m.split("=")[1]),
        "a": int(a.split("=")[1]),
        "s": int(s.split("=")[1])
    })

rules = {}
for rule_input in rules_input:
    id,ruleset = rule_input[:-1].split("{")
    ruleset = ruleset.split(",")
    r_list = []
    for r in ruleset:
        if id == "in":
            print(r, ">" in r)
        if ">" in r:
            char,cond = r.split(">")
            cond,res = cond.split(":")
            r_list.append([char, "gt", int(cond), res])
        elif "<" in r:
            char,cond = r.split("<")
            cond,res = cond.split(":")
            r_list.append([char, "lt", int(cond), res])
        else:
            r_list.append([None, None,None,r])
    if id == "in":
        print(ruleset, r_list)
    rules[id] = r_list

accepted = []

def follow_rule(part, rules):
    res = None
    while res not in ["A", "R"]:
        if not res:
            ruleset = rules["in"]
        else:
            ruleset = rules[res]
    
        for rule in ruleset:
            match rule:
                case [char, "lt", cond, result]:
                    if part[char] < cond:
                        res = result
                        break
                case [char, "gt", cond, result]:
                    if part[char] > cond:
                        res = result
                        break
                case [None, None, None, result]:
                    res = result
                    break
                
    return res == "A"

def recurse_rule(ranges, res, rules):
    if res == "A":
        accepted.append(ranges)
        return
    if res == "R":
        return
    
    ruleset = rules[res]
    for rule in ruleset:
        match rule:
            case [char, operator, cond, result] if operator in ["gt", "lt"]:
                new_ranges = deepcopy(ranges)

                current_char_range = ranges[char]

                lower_bound = set(range(1,cond + 1))
                upper_bound = set(range(cond, 4001))

                if operator == "lt":
                    new_char_range = current_char_range.difference(upper_bound)
                elif operator == "gt":
                    new_char_range = current_char_range.difference(lower_bound)

                new_ranges[char] = current_char_range.difference(new_char_range)

                recurse_rule(new_ranges, result, rules)
            case [None, None, None, result]:
                recurse_rule(deepcopy(ranges), result, rules)
                
        

accepted = []
for part in parts:
    if follow_rule(part, rules):
        accepted.append(part["x"] + part["m"] + part["a"] + part["s"])

print(sum(accepted))

ranges = {"x": set(range(1,4001)), "m": set(range(1,4001)), "a": set(range(1,4001)), "s": set(range(1,4001))}

accepted = []
recurse_rule(ranges, "in", rules)

total = 0
for r in accepted:
    val = 1
    for vals in r.values():
        val *= len(vals)
    total += val
print(total)