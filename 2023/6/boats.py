import math

input = [(34,204),(90,1713), (89,1210), (86,1780)]
input2 = [(34908986,204171312101780)]
record_breaking = []
for time,distance in input:
    records = 0
    for hold in range(0,time+1):
        potential_dist = (time - hold) * hold
        records += 1 if potential_dist > distance else 0
    record_breaking.append(records)

print(math.prod(record_breaking))

