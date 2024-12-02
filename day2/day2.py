
def part1():
    # read input file
    reports = []
    with open('day2/input.txt') as file:
        for line in file:
            reports.append([int(item) for item in line.split()])

    result = 0
    for report in reports:
        # check if report is ascending or descendng
        # check if the difference between each element is less than or equal to 3
        is_ascending = all((report[i] < report[i + 1]) and (report[i+1] - report[i] <= 3) for i in range(len(report) - 1))
        is_descending = all((report[i] > report[i + 1]) and (report[i] - report[i+1] <= 3) for i in range(len(report) - 1))
        if is_ascending or is_descending:
            result += 1

    return result


print(part1())
