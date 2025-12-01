def transpose(mirror):
    return list(map(list, zip(*mirror)))

def get_reflections(mirror):
    reflections = 0
    lines = ["".join(m) for m in mirror]
    reflect_idxs = []
    for idx,line in enumerate(lines[:-1]):
        if line == lines[idx+1]:
            reflect_idxs.append((idx, idx+1))
    
    for idx1,idx2 in reflect_idxs:
        print(idx1, idx2, lines[idx1], lines[idx2])
        i, j = idx1 - 1, idx2 + 1
        is_broken = False
        while i >= 0 and j < len(lines):
            print(i, j, lines[i], lines[j])
            if lines[i] != lines[j]:
                is_broken = True
                break
            i -= 1
            j += 1
        if len(lines)%2 and is_broken:
            if j - i == len(lines) - 1:
                reflections = idx1 + 1
        elif not is_broken:
            reflections = idx1 + 1
        if reflections:
            return reflections

    return reflections

def fix_smudge(y, x, mirror):
    new_mirror = mirror
    print(mirror, y, x)
    if mirror[y][x] == ".":
       new_mirror[y][x] = "#"
    else:
       new_mirror[y][x] = "."
    return new_mirror

def brute_force(mirror, part1):
    new_row, new_col = set(), set()
    for y in range(len(mirrors)+1):
        for x in range(len(mirrors[0])+1):
            new_row_mirror = fix_smudge(y, x, mirror)
            new_col_mirror = transpose(new_row_mirror)

            if part1["row"]:
                new_row_reflections = get_reflections(new_row_mirror)
                if part1["row"] != new_row_reflections:
                    new_row.add(new_row_reflections)
            if part1["col"]:
                new_col_reflections = get_reflections(new_col_mirror)
                if part1["col"] != new_col_reflections:
                    new_col.add(new_col_reflections)

    print(new_row, new_col)
    # return (new_row*100) + new_col
    return 0




mirrors = []
with open("test.txt") as f:
    entry = []
    for line in f:
        line = line.strip()
        if line:
            entry.append([c for c in line])
        else:
            mirrors.append(entry)
            entry = []

col_reflections = 0
row_reflections = 0
totals = []
part_1 = {}
for idx,mirror in enumerate(mirrors):
    row_reflections = get_reflections(mirror)
    col_reflections = get_reflections(transpose(mirror))
    totals.append((row_reflections*100) + col_reflections)
    part_1[idx] = {"row": row_reflections if row_reflections else None, "col": col_reflections if col_reflections else None}

print(sum(totals))
print(part_1)

part_2 = []
for idx, mirror in enumerate(mirrors):
    reflections = brute_force(mirror, part_1[idx])
    part_2.append(reflections)

print(sum(part_2))
