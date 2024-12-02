
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

def part2():
    # read input file
    reports = []
    with open('day2/input.txt') as file:
        for line in file:
            reports.append([int(item) for item in line.split()])

    result = 0

    def is_ordered(segment):
        asc = all(segment[i] < segment[i+1] and abs(segment[i+1] - segment[i]) <= 3 for i in range(len(segment) - 1))
        desc = all(segment[i] > segment[i+1] and abs(segment[i] - segment[i+1]) <= 3 for i in range(len(segment) - 1))
        return asc or desc

    for report in reports:
        # check if the whole report is ordered
        if is_ordered(report):
            result += 1
        else:
            # try removing one element to see if it becomes ordered
            for j in range(len(report)):
                modified_report = report[:j] + report[j+1:]
                if is_ordered(modified_report):
                    result += 1
                    break  # found a valid configuration, no need to try removing more elements

    return result


print(part1())
print(part2())
