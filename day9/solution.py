filename = 'data.txt'
from numpy import sign


class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def moveUp(self):
        self.y += 1

    def moveDown(self):
        self.y -= 1

    def moveRight(self):
        self.x += 1

    def moveLeft(self):
        self.x -= 1

    def isAdjecent(self, other):
        if abs(self.x - other.x) <= 1 and abs(self.y - other.y) <= 1:
            return True
        return False

    def isInSameColumn(self, other):
        if self.y == other.y:
            return True
        return False

    def isInSameRow(self, other):
        if self.x == other.x:
            return True
        return False

    def getXDifference(self, other):
        return self.x - other.x

    def getYDifference(self, other):
        return self.y - other.y


class Head:
    def __init__(self, position):
        self.position = position

    def moveIn(self, direction):
        if direction == "R":
            self.position.moveRight()
        elif direction == "L":
            self.position.moveLeft()
        elif direction == "D":
            self.position.moveDown()
        elif direction == "U":
            self.position.moveUp()


class Tail:
    def __init__(self, position):
        self.position = position
        self.all_positions = []
        self.all_positions.append((self.position.x, self.position.y))

    def isDiagonalMove(self, head):
        if not self.position.isInSameColumn(head.position) and \
           not self.position.isInSameRow(head.position):
            return True
        return False

    def changeColumnIf(self, x_difference):
        if x_difference > 1:
            self.position.moveLeft()
        elif x_difference < -1:
            self.position.moveRight()

    def changeRowIf(self, y_difference):
        if y_difference > 1:
            self.position.moveDown()
        elif y_difference < -1:
            self.position.moveUp()

    def diagonalMove(self, head):
        x_difference = self.position.getXDifference(head.position)
        y_difference = self.position.getYDifference(head.position)
        x = sign(x_difference)
        y = sign(y_difference)
        self.position.x -= x
        self.position.y -= y

    def makeMove(self, head):
        x_difference = self.position.getXDifference(head.position)
        y_difference = self.position.getYDifference(head.position)
        self.changeColumnIf(x_difference)
        self.changeRowIf(y_difference)

    def follow(self, head):
        if not self.position.isAdjecent(head.position):
            if not self.isDiagonalMove(head):
                self.makeMove(head)
                self.all_positions.append((self.position.x, self.position.y))
            else:
                self.diagonalMove(head)
                self.all_positions.append((self.position.x, self.position.y))

    def getPositionsSet(self):
        return set(self.all_positions)

    def printAllPositions(self):
        positions = self.getPositionsSet()
        for i in positions:
            print(i)

    def printSolution(self, task_id):
        positions = self.getPositionsSet()
        print("Task ", task_id, ": ", len(positions))


def parseData(line):
    t = []
    t = line.split(' ')
    return t[0], int(t[1])


def makeSingleMove(direction, steps, head, tail):
    for i in range(steps):
        head.moveIn(direction)
        tail.follow(head)


def main():
    f = open(filename, 'r')
    head = Head(Position(0, 0))
    tail = Tail(Position(0, 0))
    for line in f:
        direction, steps = parseData(line)
        makeSingleMove(direction, steps, head, tail)
    tail.printSolution(1)


def makeAllMoves(direction, steps, leader, followers):
    for i in range(steps):
        leader.moveIn(direction)
        followers[0].follow(leader)
        for f in range(1, len(followers)):
            makeFollowerMove(followers[f - 1], followers[f])


def makeFollowerMove(leader, follower):
    follower.follow(leader)


def makeFollowerList(N=9):
    followers = []
    for i in range(N):
        followers.append(Tail(Position(0, 0)))
    return followers


def main_part2():
    f = open(filename, 'r')
    head = Head(Position(0, 0))
    followers = makeFollowerList()
    for line in f:
        direction, steps = parseData(line)
        makeAllMoves(direction, steps, head, followers)
    followers[-1].printSolution(2)


main()
main_part2()
