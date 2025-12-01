histories = []
with open("input.txt") as f:
    for line in f:
        histories.append([eval(c) for c in line.strip().split(" ")])

print(histories)

next_numbers = []
prev_numbers = []
for history in histories:
    previous_lists = []
    index = 0
    diff = 0
    current_list = history
    while len(set(current_list)) > 1:
        new_list = [current_list[idx+1] - e for idx,e in enumerate(current_list) if idx+1 < len(current_list)]
        previous_lists.append(current_list)
        index += 1
        current_list = new_list

    last_list = current_list
    last_list2 = current_list
    
    for current_list in previous_lists[::-1]:
        next_element = last_list[-1] + current_list[-1]
        current_list.append(next_element)
        last_list = current_list
        print(current_list)

    next_numbers.append(next_element)

    for current_list in previous_lists[::-1]:
        prev_element = current_list[0] - last_list2[0]
        current_list = [prev_element] + current_list
        last_list2 = current_list
        print(current_list)

    prev_numbers.append(prev_element)
    print(prev_element)

print(sum(next_numbers))
print(sum(prev_numbers))