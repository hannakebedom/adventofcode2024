from collections import defaultdict

def part1():
    # read input file
    left, right  = [], []
    with open('day1/input.txt') as file:
        for line in file:
            nums = line.split()
            left.append(int(nums[0]))
            right.append(int(nums[1]))

    # sort both lists
    left.sort()
    right.sort()

    # calculate the difference between each element
    result = 0
    for i in range(len(left)):
        # sum the absolute difference between each element
        result += abs(left[i] - right[i])

    return result

def part2():
    # read input file
    left, right  = [], []
    with open('day1/input.txt') as file:
        for line in file:
            nums = line.split()
            left.append(int(nums[0]))
            right.append(int(nums[1]))

    # iterate through each number on the left
    right_count = defaultdict(int)
    result = 0
    for num in left:
        # count the number of times num appears in right
        if num not in right_count:
            right_count[num] = right.count(num)
        result += num * right_count[num]
    return result

print(part1())
print(part2())
