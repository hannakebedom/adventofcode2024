import collections
import networkx as nx

def part1():
    guide = collections.defaultdict(set)
    updates = []

    with open('day5/example.txt') as file:
        for line in file:
            if "|" in line:
                first, second = line.split("|")
                guide[int(first)].add(int(second))
            elif line != "\n":
                updates.append([int(num) for num in line.strip().split(",")])

    correct_updates = []

    # identify which updates are in the right order
    for update in updates:
        correct_order = True
        for i in range(len(update)):
            if guide[update[i]].intersection(set(update[:i])):
                correct_order = False
                break
        if correct_order:
            correct_updates.append(update)

    result = 0
    # sum the middle page number of those updates
    for update in correct_updates:
        middle_index = len(update) // 2
        result += update[middle_index]

    return result

print(part1())

def part2():
    guide = collections.defaultdict(set)
    updates = []

    with open('day5/input.txt') as file:
        for line in file:
            if "|" in line:
                first, second = line.split("|")
                guide[int(first)].add(int(second))
            elif line != "\n":
                updates.append([int(num) for num in line.strip().split(",")])

    incorrect_updates = []

    # identify which updates are in the right order
    for update in updates:
        correct_order = True
        for i in range(len(update)):
            if guide[update[i]].intersection(set(update[:i])):
                correct_order = False
                incorrect_updates.append(update)
                break


    print("Incorrect updates:", incorrect_updates)

    ordered_updates =  []
    for update in incorrect_updates:
        G = nx.DiGraph()
        for key, value in guide.items():
            if key in update:
                for v in value:
                    if v in update:
                        G.add_edge(key, v)

        try:
            order = list(nx.topological_sort(G))
            ordered_updates.append(order)
            print("Topological order:", order)
        except nx.NetworkXUnfeasible:
            print("No topological order possible (there's a cycle in the graph).")

    print("Ordered updates:", ordered_updates)

    result = 0

    for update in ordered_updates:
        middle_index = len(update) // 2
        result += update[middle_index]

    return result


print(part2())

