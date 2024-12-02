def part1():
    # read input file
    a, b  = [], []
    with open('day1/input.txt') as file:
        for line in file:
            nums = line.split()
            a.append(int(nums[0]))
            b.append(int(nums[1]))

    # sort both lists
    a.sort()
    b.sort()

    # calculate the difference between each element
    result = 0
    for i in range(len(a)):
        # sum the absolute difference between each element
        result += abs(a[i] - b[i])

    return result

print(part1())
