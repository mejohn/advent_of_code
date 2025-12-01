
inputt = []
with open("input_1.txt", "r") as f:
    for line in f:
        inputt.append(line.strip())

digits = []
for line in inputt:
    line_digits = []
    for char in line:
        if char.isdigit():
            line_digits.append(char)
    digits.append(line_digits)

sum = 0
for line in digits:
    number = eval("".join([line[0], line[-1]]))
    sum += number
       
print(sum)

can_overlap = {
    "oneight": "oneeight",
    "eighthree": "eightthree",
    "threeight": "threeeight",
    "twone": "twoone",
    "sevenine": "sevennine",
    "nineight": "nineeight",
    "fiveight": "fiveeight",
    "oneight": "oneeight",
    "eightwo": "eighttwo",
}
mapping = {
    "one": "1",
    "two": "2", 
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

replaced = []
for line in inputt:
    new_line = line
    for squish,separ in can_overlap.items():
        if squish in line:
            new_line = new_line.replace(squish,separ)
    for name,num in mapping.items():
        if name in new_line:
            new_line = new_line.replace(name, num)
    replaced.append(new_line)

digits = []
for line in replaced:
    line_digits = []
    for char in line:
        if char.isdigit():
            line_digits.append(char)
    digits.append(line_digits)

sum = 0
for line in digits:
    number = eval("".join([line[0], line[-1]]))
    sum += number

print(sum)
