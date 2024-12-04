import re

pattern_1 = r"mul\((\d+),(\d+)\)"

def part1():
    with open('day3/input.txt') as file:
        lines = file.readlines()  # Read all lines into a list
        text = ''.join(line.strip() for line in lines)  # Strip each line and join into a single string

    matches = re.findall(pattern_1, text)
    mul_enabled = True
    result = 0

    for match in matches:
        first = int(match[0])
        second = int(match[1])
        result += first * second
    return result

pattern_2 = r"mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))"

def part2():
    with open('day3/input.txt') as file:
        lines = file.readlines()  # Read all lines into a list
        text = ''.join(line.strip() for line in lines)  # Strip each line and join into a single string

    matches = re.findall(pattern_2, text)
    mul_enabled = True
    result = 0

    for match in matches:
        if match[2]:
            mul_enabled = True
        elif match[3]:
            mul_enabled = False
        else:
            first = int(match[0])
            second = int(match[1])
            if mul_enabled:
                result += first * second
    return result

print(part1())
print(part2())



