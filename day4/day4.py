import numpy as np

def part1():
    rows = []
    with open('day4/input.txt') as file:
        for line in file:
            rows.append(line.strip())

    result = 0

    # horizontal
    for row in rows:
        result += row.count("XMAS") + row.count("XMAS"[::-1])

    # vertical
    columns = ['' for _ in range(len(rows[0]))]
    for i in range(len(rows)):
        row = rows[i]
        for j in range(len(row)):
            columns[j] += row[j]

    for column in columns:
        result += column.count("XMAS") + column.count("XMAS"[::-1])

    # diagonal
    rows = np.array([list(row) for row in rows])
    for i in range(-len(rows) + 1, len(rows[0])):
        diagonal = ''.join(rows.diagonal(i))
        result += diagonal.count("XMAS") + diagonal.count("XMAS"[::-1])

    # anti-diagonal
    rows_flipped = np.fliplr(rows)
    for i in range(-len(rows) + 1, len(rows[0])):
        anti_diagonal = ''.join(rows_flipped.diagonal(i))
        result += anti_diagonal.count("XMAS") + anti_diagonal.count("XMAS"[::-1])


    return result


print(part1())
