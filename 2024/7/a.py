from functools import reduce
from operator import mul

lines = []
with open("input.txt") as f:
    for line in f:
        lines.append(line.strip())

ops = {}
res = 0
for line in lines:
    ans,nums = line.split(":")
    nums = nums.strip().split(" ")
    key = int(ans)
    ops[key] = [int(num) for num in nums]
    if key == sum(ops[key]) or key == reduce(mul, ops[key]):
        print(key, ops[key], sum(ops[key]), reduce(mul, ops[key]))
        res += key
    else:
        test_vals = []
        for i in range(1, len(ops[key])):
            if not test_vals:
                test_vals.append(
                    ops[key][i-1] + ops[key][i]
                )
                test_vals.append(
                    ops[key][i-1] * ops[key][i]
                )
            else:
                for j in range(0, len(test_vals)):
                    old_val = test_vals[j]
                    test_vals[j] += ops[key][i]
                    test_vals.append(old_val * ops[key][i])
                if any(val for val in test_vals if val == key):
                    print(key, ops[key])
                    res += key
print(res)