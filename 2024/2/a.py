from copy import deepcopy


lines = []
with open("input.txt") as f:
    for line in f:
        lines.append([int(x) for x in line.strip().split(" ")])

safes = []
retry = []
for report in lines:
    diff = report[1] - report[0]
    unsafe = 0
    unsafe_idxs = []
    inc = diff > 0
    for idx in range(1, len(report)+1):
        # print(diff, inc, report[idx],report[idx-1])
        if abs(diff) > 3 or abs(diff) == 0:
            unsafe += 1
            unsafe_idxs.extend([idx-1, idx-2])

        if diff < 0 and inc or diff > 0 and not inc:
            unsafe +=1
            unsafe_idxs.extend([idx-2, idx-1])

        if len(report) > idx:
            diff = report[idx] - report[idx-1]

    if unsafe == 0:
        safes.append(report)
    else:
        retry.append(report)

print(len(safes))
print(retry)

safe_retries = []
for report in retry:
    for unsafe_idx in range(0,len(report)):
        new_report = deepcopy(report)
        new_report.pop(unsafe_idx)
        print(new_report)
        diff = new_report[1] - new_report[0]
        unsafe = 0
        inc = diff > 0
        for idx in range(1, len(new_report)+1):
            if abs(diff) > 3 or abs(diff) == 0:
                unsafe += 1
            if diff < 0 and inc or diff > 0 and not inc:
                unsafe +=1
            if len(new_report) > idx:
                diff = new_report[idx] - new_report[idx-1]
                print(diff, inc, new_report[idx],new_report[idx-1], unsafe, idx)


        if unsafe == 0:
            safe_retries.append(report)
            break
        
print(len(retry), len(safe_retries), safe_retries)
print(len(safe_retries) + len(safes))