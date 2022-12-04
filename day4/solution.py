filename = 'data.txt'


def sortPairBySmaller(left, right):
    if left[0] < right[0]:
        return left, right
    elif left[0] > right[0]:
        return right, left
    if left[1] > right[1]:
        return left, right
    return right, left


def splitToPair(new_line):
    pair = new_line.split('-')
    return (int(pair[0]), int(pair[1]))


def splitLineToLeftRight(line):
    new_line = line.split(',')
    left = splitToPair(new_line[0])
    right = splitToPair(new_line[1])
    return sortPairBySmaller(left, right)


def main():
    f = open(filename, 'r')
    counter = 0
    counter_task_2 = 0
    for line in f:
        left, right = splitLineToLeftRight(line)
        if isOverlap(left, right):
            if isFullyContained(left, right):
                counter += 1
            counter_task_2 += 1
    print("Task 1: ", counter)
    print("Task 2: ", counter_task_2)


def isFullyContained(left, right):
    if left[1] >= right[1]:
        return True
    return False


def isOverlap(left, right):
    if right[0] <= left[1]:
        return True
    return False


main()
