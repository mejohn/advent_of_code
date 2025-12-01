def check_digits(i,j):
    has_digit = set()
    if columns[i-1][j].isdigit():
        has_digit.add((i-1,j))
    if columns[i-1][j-1].isdigit():
        has_digit.add((i-1,j-1))
    if columns[i-1][j+1].isdigit():
        has_digit.add((i-1,j+1))
    if columns[i][j-1].isdigit():
        has_digit.add((i,j-1))
    if columns[i+1][j].isdigit():
        has_digit.add((i+1,j))
    if columns[i+1][j+1].isdigit():
        has_digit.add((i+1,j+1))
    if columns[i][j+1].isdigit():
        has_digit.add((i,j+1))    
    if columns[i+1][j-1].isdigit():
        has_digit.add((i+1,j-1))
    return has_digit

def eval_num(checked_indexes, i,j):
    if (i,j) not in checked_indexes:
        if not columns[i][j-1].isdigit():
            # look right 2 spaces
            if not columns[i][j+1].isdigit():
                checked_indexes.update([(i,j),(i,j+1)])
                num = [columns[i][j]]
            elif not columns[i][j+2].isdigit():
                checked_indexes.update([(i,j), (i, j+1), (i,j+2)])
                num = [columns[i][j], columns[i][j+1]]
            else:
                checked_indexes.update([(i,j-1),(i,j),(i,j+1),(i,j+2),(i,j+3)])
                num = [columns[i][j], columns[i][j+1], columns[i][j+2]]
        elif not columns[i][j+1].isdigit():
            # look left 2 spaces
            if not columns[i][j-1].isdigit():
                checked_indexes.update([(i,j),(i,j-1)])
                num = [columns[i][j]]
            elif not columns[i][j-2].isdigit():
                checked_indexes.update([(i,j), (i, j-1), (i,j-2)])
                num = [columns[i][j-1], columns[i][j]]
            else:
                checked_indexes.update([(i,j+1),(i,j),(i,j-1),(i,j-2),(i,j-3)])
                num = [columns[i][j-2], columns[i][j-1], columns[i][j]]
        else:
            # look 1 left and 1 right
            checked_indexes.update([(i,j-2),(i,j-1),(i,j),(i,j+1),(i,j+2)])
            num = [columns[i][j-1],columns[i][j],columns[i][j+1]]
        return checked_indexes,num
    return checked_indexes,None


columns = []
with open("input_3.txt") as f:
    for line in f:
        columns.append(["a"] + [c if c != "." else "a" for c in line.strip() ] + ["a"])

columns = [["a"]*len(columns[0])] + columns + [["a" ]*len(columns[0])]

symbols = ["!", "@", "#", "$", "^", "&", "*", "/", "-", "="]

symbols_lookup = []
gears_lookup = []
for i,column in enumerate(columns):
    for j,row in enumerate(column):
        if not columns[i][j].isdigit() and columns[i][j] != "a":
            if columns[i][j] != "*":
                symbols_lookup.append((i, j))
            else:
                gears_lookup.append((i,j))

has_digit = set()
for i,j in symbols_lookup:
    # check adjacency for digits, deduplicated
    # no symbols on first or last char, don't bother with edge cases
    has_digit.update(check_digits(i,j))

gears_digit = []
for i,j in gears_lookup:
    digits = list(check_digits(i,j))
    print(i,j,digits)
    if len(digits) == 2:
        gears_digit.append(digits)
    if len(digits) >= 2:
        pair1 = digits[0]
        for digit in digits[1:]:
            if digit[0] != pair1[0]:
                pair2 = digit
        print(pair1, pair2)
        gears_digit.append((pair1,pair2))
    else:
        has_digit.update(digits)

gear_numbers = []
part_numbers = []
checked_indexes = set()
for one,two in gears_digit:
    checked_indexes,num1 = eval_num(checked_indexes,one[0],one[1])
    checked_indexes,num2 = eval_num(checked_indexes,two[0],two[1])
    if num1 and num2:
        gear_numbers.append(int(eval("".join(num1)))*int(eval("".join(num2))))
    elif num1:
        part_numbers.append(int(eval("".join(num1))))
    elif num2:
        part_numbers.append(int(eval("".join(num2))))


# print(has_digit)

for i,j in has_digit:
    # no numbers more than 3 digits.
    checked_indexes,num = eval_num(checked_indexes, i, j)
    if num:
        part_numbers.append(int(eval("".join(num))))

print(sum(gear_numbers))