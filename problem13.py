
def main():
    with open("input13.txt") as file:
        lines = file.readlines()

    lines = [line.replace('\n','') for line in lines]

    packets = []
    for line in lines:
        if line != '':
            packets.append(eval(line))

    # part one
    counter = 0
    answer = 0
    packet_count = len(packets) - 1
    for i in range(0,packet_count,2):
        counter += 1
        check = compare(packets[i], packets[i + 1])
        if check:
            answer += counter

    print(answer)
    # part two

    packets.append([[2]])
    packets.append([[6]])

    packet_count = len(packets)
    for _ in range(packet_count):
        for i in range(packet_count - 1):
            if not compare(packets[i], packets[i+1]):
                packets[i], packets[i+1] = packets[i+1], packets[i]

    key = 1
    for i in range(packet_count):
        if packets[i] in [[[2]],[[6]]]:
            key *= (i + 1)
    
    print(key)
 


def compare(one, two):
    if isinstance(one, int) and isinstance(two, int):   
        if one < two:
            return True
        elif one > two:
            return False
        else:
            return None
    elif isinstance(one, int) and isinstance(two, list):
        return compare([one], two)
    elif isinstance(one, list) and isinstance(two, int):
        return compare(one, [two])
    elif isinstance(one, list) and isinstance(two, list):
        i = 0
        check = None
        while check == None:
            try:
                check = compare(one[i], two[i])
                i += 1
            except IndexError:
                if len(one) < len(two):
                    return True
                elif len(one) == len(two):
                    return None
                elif len(one) > len(two):
                    return False
        return check

        
if __name__ == "__main__":
    main()