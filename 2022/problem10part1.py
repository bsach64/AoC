import re

signal_strengths = []
answer = 0  
current_register_value = 1
register_values = []

with open("InputDay10", "r") as file:
    for line in file:
        if re.match("^noop", line):
            register_values.append(current_register_value)
        elif re.match("^addx", line):
            register_values.append(current_register_value)
            number = re.findall('-?\d+\.?\d*', line)
            current_register_value = current_register_value + int(number[0])
            register_values.append(current_register_value)


signal_strengths.append(20 * register_values[18])
signal_strengths.append(60 * register_values[58])
signal_strengths.append(100 * register_values[98])
signal_strengths.append(140 * register_values[138])
signal_strengths.append(180 * register_values[178])
signal_strengths.append(220 * register_values[218])


for i in range(0, len(signal_strengths)):
    print(signal_strengths[i])
    answer = answer + signal_strengths[i]

print(answer)