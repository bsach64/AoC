import re

def main():
    CRT_screen = []
    sprite_postion = 1
    crt_counter = 0
    noop_count = 0
    addx_count = 0
    with open("InputDay10", "r") as file:
        for line in file:
            if re.match("^noop", line):
                noop_count = noop_count + 1
                comp(crt_counter, sprite_postion, CRT_screen)
                crt_counter = crt_counter + 1
                if crt_counter == 40:
                    crt_counter = 0
            elif re.match("^addx", line):
                addx_count = addx_count + 1
                comp(crt_counter, sprite_postion, CRT_screen)
                crt_counter = crt_counter + 1
                if crt_counter == 40:
                    crt_counter = 0
                comp(crt_counter, sprite_postion, CRT_screen)
                crt_counter = crt_counter + 1
                if crt_counter == 40:
                    crt_counter = 0
                number = re.findall('-?\d+\.?\d*', line)
                sprite_postion = sprite_postion + int(number[0])
    print(noop_count)
    print(addx_count)
    print(len(CRT_screen))
    final_screen = []
    for i in range(0, 6):
        final_screen.append([])
    final_screen[0] = CRT_screen[0:40]
    final_screen[1] = CRT_screen[40:80]
    final_screen[2] = CRT_screen[80:120]
    final_screen[3] = CRT_screen[120:160]
    final_screen[4] = CRT_screen[160:200]
    final_screen[5] = CRT_screen[200:240]

    for i in range(0,6):
        result = ''.join(str(item) for item in final_screen[i])
        print(result)
    

def comp(a , b, list = []):
    if a == b:
        list.append('#')
    elif a == (b + 1):
        list.append('#')
    elif a == (b - 1):
        list.append('#')
    else:
        list.append('.')


main()