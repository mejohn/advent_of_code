with open("input.txt") as f:
    line = f.read().strip()

filesystem = ""
current_id = 0
block = True
id_mapping = {}
unoccupied = []
for char in line:
    if block:
        filesystem += "#"*int(char)
        id_mapping[current_id] = list(range(len(filesystem)-int(char), len(filesystem)))
        current_id += 1
        block = False
    else:
        filesystem += "."*int(char)
        unoccupied.append(list(range(len(filesystem)-int(char), len(filesystem))))
        block=True
    
print(filesystem)
print(id_mapping)
print(unoccupied)

squish = [c for c in filesystem]
print(squish)

current_id -= 1

while current_id:
    current_positions = id_mapping[current_id]
    for r_idx,region in enumerate(unoccupied):
        if len(current_positions) <= len(region) and current_positions[0] > region[0]:
            new_positions = region[:len(current_positions)]
            id_mapping[current_id] = new_positions
            unoccupied[r_idx] = region[len(current_positions):]
            if not unoccupied[r_idx]:
                unoccupied.remove(unoccupied[r_idx])
            print(unoccupied)
            break
    current_id -= 1



checksum = 0
for id,idxs in id_mapping.items():
    print(id, idxs )
    checksum += sum([id*idx for idx in idxs])

print(checksum)