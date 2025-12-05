ranges = []
items = []

add_to_items = False
with open("input_5.txt") as f:
    for line in f:
        if line.strip() == "":
            add_to_items = True
            continue
        if not add_to_items:
            left,right = line.strip().split("-")
            r = range(int(left), int(right)+1)
            ranges.append(r)
        else:
            items.append(int(line.strip()))

fresh = set()
for item in items:
    for r in ranges:
        if item in r:
            fresh.add(item)
            break

print("Part 1: ", len(fresh))

copy_ranges = sorted([(r.start, r.stop) for r in ranges], key=lambda x: (x[0], -x[1]))
copy_ranges = [range(r[0], r[1]) for r in copy_ranges]
shrink_ranges = []
for r in copy_ranges:
    min_r, max_r = r.start, r.stop
    add = True
    for idx,next_r in enumerate(shrink_ranges):
        if min_r in next_r:
            if max_r > next_r.stop:
                shrink_ranges[idx] = range(next_r.start, max_r)
            add = False
        elif max_r in next_r:
            if min_r < next_r.start:
                shrink_ranges[idx] = range(min_r, next_r.stop)
            add = False

    if add:
        shrink_ranges.append(r)
print("Part 2: ", sum([len(r) for r in shrink_ranges]))
