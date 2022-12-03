filename = 'data.txt'


def divideToTwoParts(line):
    left = line[:(len(line)) // 2]
    right = line[(len(line)) // 2:]
    return left, right


def findCommonLetter(left, right):
    for letter in left:
        if letter in right:
            return letter


def scoreLettersPriority(letter):
    score = ord(letter)
    if score > 95:
        return score - 96
    return score - 38


def task1():
    f = open(filename, 'r')
    score = 0
    for line in f:
        left, right = divideToTwoParts(line)
        letter = findCommonLetter(left, right)
        score += scoreLettersPriority(letter)
    print("Task 1: ", score)


def getGroupOfThree(group_members, group, line):
    if not group_members:
        group.clear()
    group.append(line)
    return group


def findGroupLetter(group):
    first = group[0]
    for letter in first:
        if letter in group[1] and letter in group[2]:
            return letter


def task2():
    f = open(filename, 'r')
    score = 0
    group_members = 0
    group = []
    for line in f:
        group = getGroupOfThree(group_members, group, line)
        group_members = (group_members + 1) % 3
        if not group_members:
            letter = findGroupLetter(group)
            score += scoreLettersPriority(letter)
    print("Task 2: ", score)


task1()
task2()
