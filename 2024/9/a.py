with open("input.txt") as f:
    line = f.read().strip()

filesystem = ""
current_id = 0
block = True
id_mapping = {}
for char in line:
    if block:
        filesystem += "#"*int(char)
        id_mapping.update({k:current_id for k in range(len(filesystem)-int(char) ,len(filesystem))})
        current_id += 1
        block = False
    else:
        filesystem += "."*int(char)
        block=True
    
print(filesystem)
print(id_mapping)

squish = [c for c in filesystem]
print(squish)
last_squish = squish
while '.' in squish:
    if squish[-1] != '.':
        last_idx = len(squish) - 1
        idx = squish.index(".")
        id_mapping[idx] = id_mapping[last_idx]
        del id_mapping[last_idx]
        squish[idx] = squish[-1]

    squish = squish[:-1]
    if last_squish == squish:
        break
    last_squish = squish
    # print("".join(squish))


checksum = 0
for idx,id in id_mapping.items():
    checksum += idx*id

print(checksum)