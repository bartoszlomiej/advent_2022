import numpy as np

filename = 'data.txt'


class TreeGrid:
    def __init__(self, all_trees):
        self.all_trees = all_trees
        self.visibility_grid = np.full_like(np.array(all_trees), True)
        self.width = len(all_trees[0])
        self.height = len(all_trees)
        self.highest_score = 1

    def countEdgeTrees(self):
        return 2 * self.width + 2 * self.height - 4  #due to repeat corner cases

    def rowSmallerThan(self, row, column):
        for i in range(row):
            if self.all_trees[i][column] >= self.all_trees[row][column]:
                return True
        return False

    def rowGreaterThan(self, row, column):
        for i in range(row + 1, self.width):
            if self.all_trees[i][column] >= self.all_trees[row][column]:
                return True
        return False

    def isRowVisible(self, row, column):
        if column > 0 and column < self.height - 1:
            if self.rowSmallerThan(row, column) and \
               self.rowGreaterThan(row, column):
                return False
        return True

    def columnSmallerThan(self, row, column):
        for i in range(column):
            if self.all_trees[row][i] >= self.all_trees[row][column]:
                return True
        return False

    def columnGreaterThan(self, row, column):
        for i in range(column + 1, self.width):
            if self.all_trees[row][i] >= self.all_trees[row][column]:
                return True
        return False

    def isColumnVisible(self, row, column):
        if row > 0 and row < self.width - 1:
            if self.columnSmallerThan(row, column) and \
               self.columnGreaterThan(row, column):
                return False
        return True

    def checkVisibility(self):
        for row in range(self.height):
            for column in range(self.width):
                if not self.isRowVisible(row, column) and \
                   not self.isColumnVisible(row, column):
                    self.visibility_grid[row][column] = False

    def countVisible(self):
        suma = 0
        for row in self.visibility_grid:
            for column in row:
                if column:
                    suma += 1
        return suma - 1

    def countRowSmaller(self, row, column):
        suma = 1
        for i in range(row - 1, -1, -1):
            if self.all_trees[i][column] >= self.all_trees[row][column]:
                return suma
            suma += 1
        return suma - 1 if suma > 1 else suma

    def countRowGreater(self, row, column):
        suma = 1
        for i in range(row + 1, self.height):
            if self.all_trees[i][column] >= self.all_trees[row][column]:
                return suma
            suma += 1
        return suma - 1 if suma > 1 else suma

    def countColumnSmaller(self, row, column):
        suma = 1
        for i in range(column - 1, -1, -1):
            if self.all_trees[row][i] >= self.all_trees[row][column]:
                return suma
            suma += 1
        return suma - 1 if suma > 1 else suma

    def countColumnGreater(self, row, column):
        suma = 1
        for i in range(column + 1, self.width):
            if self.all_trees[row][i] >= self.all_trees[row][column]:
                return suma
            suma += 1
        return suma - 1 if suma > 1 else suma

    def evaluateSceneScore(self, row, column):
        scene_score = self.countRowSmaller(row, column) * \
            self.countRowGreater(row, column) * \
            self.countColumnSmaller(row, column) *\
            self.countColumnGreater(row, column)
        return scene_score

    def evaluateBestScore(self):
        for row in range(self.height):
            for column in range(self.width):
                new_score = self.evaluateSceneScore(row, column)
                if new_score > self.highest_score:
                    self.highest_score = new_score
        return self.highest_score


def readData(all_trees):
    f = open(filename, 'r')
    for line in f:
        row = []
        for i in line:
            if i != "\n":
                row.append(int(i))
        all_trees.append(row)


def main():
    all_trees = []
    readData(all_trees)
    task = TreeGrid(all_trees)
    task.checkVisibility()

    print("Task 1:", task.countVisible())
    print("Task 2:", task.evaluateBestScore())


main()
