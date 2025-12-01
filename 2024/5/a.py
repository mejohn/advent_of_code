from collections import deque


rules = []
updates = []
with open("input.txt") as f:
    for line in f:
        if '|' in line:
            rules.append([int(x) for x in line.strip().split("|")])
        elif ',' in line:
            updates.append([int(x) for x in line.strip().split(',')])

print(rules, updates)

ordered = []
unordered = []
for pages in updates:
    safe = True
    for rule in rules:
        if rule[0] in pages and rule[1] in pages:
            if pages.index(rule[1]) < pages.index(rule[0]):
                if pages not in unordered:
                    unordered.append(pages)
                safe = False
    if safe:
        ordered.append(pages)

print(ordered)

sum = 0
for o in ordered:
    sum += o[int(len(o)/2)]

print(sum)
            
# o_rules = []
# print(sorted(rules))
# for rule in sorted(rules):
#     if rule[0] in o_rules and rule[1] in o_rules:
#         if o_rules.index(rule[0]) > o_rules.index(rule[1]):
#             i1 = o_rules.index(rule[1])
#             i2 = o_rules.index(rule[0])
#             o_rules[i1] = rule[0]
#             o_rules[i2] = rule[1]
#     elif rule[0] in o_rules:
#         o_rules.insert(o_rules.index(rule[0])+1, rule[1])
#     elif rule[1] in o_rules:
#         o_rules.insert(o_rules.index(rule[1]), rule[0])
#     else:
#         o_rules.append(rule[0])
#         o_rules.append(rule[1])

# print(o_rules)

# sum2 = 0        
# for u in unordered:
#     n = list(sorted(u, key=lambda x: o_rules.index(x)))
#     sum2 += n[int(len(n)/2)]

# print(sum2)

def is_ordered(u, rules):
    for rule in rules:
        if rule[0] in u and rule[1] in u:
            if u.index(rule[0]) > u.index(rule[1]):
                return False
    return True

rules = list(sorted(rules))
sum2 = 0
for n in unordered:
    u = n
    safe = False
    while not safe:
        for a,b in rules:
            print(u, n, a, b)
            if a in u and b in u and u.index(a) > u.index(b):
                ai = u.index(a)
                bi = u.index(b)
                u[ai] = b
                u[bi] = a
        safe = is_ordered(u, rules)

    sum2 += u[int(len(u)/2)]

print(sum2)
    
            

            
