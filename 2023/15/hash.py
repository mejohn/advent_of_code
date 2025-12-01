from collections import deque

inputs = []
with open("input.txt") as f:
    inputs = f.readline().strip().split(",")

print(inputs)

output = {}
sums = []
for phrase in inputs:
    phrase_num = 0
    for char in phrase:
        phrase_num += ord(char)
        phrase_num *= 17
        phrase_num = phrase_num % 256
    output[phrase] = phrase_num
    sums.append(phrase_num)


print(sum(sums))

def get_hash(label):
    phrase_num = 0
    for char in label:
        phrase_num += ord(char)
        phrase_num *= 17
        phrase_num = phrase_num % 256
    return phrase_num

print(output)
boxes = {}
for phrase in inputs:
    if "-" in phrase:
        label = phrase[:-1]
        box_num = get_hash(label)
        if box_num in boxes:
            if label in boxes[box_num]:
                del boxes[box_num][label]
    else:
        label = phrase.split("=")[0]
        box_num = get_hash(label)
        focal_length = int(phrase[-1])
        if not box_num in boxes:
            boxes[box_num] = {label: focal_length}
        elif label in boxes[box_num]:
            boxes[box_num][label] = focal_length
        else:
            boxes[box_num][label] = focal_length

focusing = []
for box,lenses in boxes.items():
    for idx,label in enumerate(lenses):
        print(1+box, idx+1, lenses[label])
        lens_focus = (1+box)*(idx+1)*lenses[label]
        print(label, lens_focus)
        focusing.append(lens_focus)

print(sum(focusing))