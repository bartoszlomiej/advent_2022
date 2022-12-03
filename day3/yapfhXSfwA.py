filename = 'test_data.txt'


def divideToTwoParts(line):
    left = line[:(len(line)) // 2]
    right = line[(len(line)) // 2:]
    return left, right


def findCommonLetter(left, right):
    for letter in left:
        if letter in right:
            return letter

    print("Mamy error byczq")


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
        group.append(line)


def task2():
    f = open(filename, 'r')
    score = 0
    group_members = 1
    group = []
    for line in f:
        group_members = group_members + 1 if group_members % 4 else 0

        left, right = divideToTwoParts(line)
        letter = findCommonLetter(left, right)
        score += scoreLettersPriority(letter)

    print("Task 1: ", score)


task1()
