data = []
with open("2.txt") as file:
    line = file.readline()
    while line:
        data.append(list(map(int, line.split())))
        line = file.readline()

def part_one(data):
    unsafe = 0
    for report in data:
        dec = False
        if report[0] > report[1]:
            dec = True
        for i in range(len(report) - 1):
            diff = report[i + 1] - report[i]
            if dec and (diff >= 0 or diff <= -4):
                unsafe += 1
                break
            elif not dec and diff <= 0 or diff >= 4:
                unsafe += 1
                break

    print(len(data) - unsafe)


def is_safe_dec(report):
    for i in range(len(report) - 1):
        diff = report[i + 1] - report[i]
        if diff >= 0 or diff <= -4:
            return False
    return True

def is_safe_inc(report):
    for i in range(len(report) - 1):
        diff = report[i + 1] - report[i]
        if diff <= 0 or diff >= 4:
            return False
    return True

def part_two(data):
    safe = 0
    for report in data:
        if is_safe_dec(report) or is_safe_inc(report):
            safe += 1
            continue
        for i in range(len(report)):
            temp = report[:i] + report[i + 1:]
            if is_safe_dec(temp) or is_safe_inc(temp):
                safe += 1
                break
    print(safe)

part_two(data)
