from copy import deepcopy

filename = "data.txt"


class Node:
    def __init__(self, value, parent):
        self.value = value
        self.nodes = []
        self.parent = parent
        self.isFinished = False

    def addChild(self, value):
        self.nodes.append(Node(value, self))
        return self.nodes[-1]

    def giveValueToParent(self):
        self.parent.value += self.value

    def checkValue(self):
        if self.value <= 100000:
            return self.value
        return 0

    def giveValueIfNotFinished(self):
        if not self.isFinished:
            self.giveValueToParent()
            self.isFinished = True


class NonBinaryTree:
    def __init__(self):
        self.root = Node(0, None)
        self.current_node = self.root.addChild(0)
        self.currently_smallest = 70000000

    def checkIfSmallest(self, node):
        minimum_required = 30000000 - 70000000 + 46592386
        if node.value < self.currently_smallest and \
           node.value >= minimum_required:
            self.currently_smallest = node.value

    def initializeTreeTraversal(self):
        self.current_node = self.root.nodes[0]
        self.treeTraversal(self.current_node, 0)

    def treeTraversal(self, c_node, level):
        for i in c_node.nodes:
            self.treeTraversal(i, level + 1)
        c_node.giveValueIfNotFinished()
        self.checkIfSmallest(c_node)
        print(c_node.value, level)


def isCommand(line):
    return True if line[0] == "$" else False


def giveScoreToLevel(line):
    t = line.split(" ")
    return int(t[0])


def changeDirectory(tree, sufix):

    if sufix[:2] == "..":
        tree.current_node.isFinished = True
        tree.current_node.giveValueToParent()
        value = tree.current_node.checkValue()
        tree.current_node = tree.current_node.parent
        return value
    tree.current_node = tree.current_node.addChild(0)
    return 0


def checkCommand(root, line):
    t = line.split(" ")
    if t[1] == 'cd':
        return changeDirectory(root, t[-1])
    return 0
    #    elif t[1] == 'ls':


def checkDirectory(tree, line):
    t = line.split(" ")
    if t[0] != "dir":
        tree.current_node.value += giveScoreToLevel(line)


def parseData(tree):
    f = open(filename, 'r')
    suma = 0
    for line in f:
        if isCommand(line):
            suma += checkCommand(tree, line)
        else:
            checkDirectory(tree, line)
    print("Task 1:", suma)


def main():
    tree = NonBinaryTree()
    parseData(tree)
    tree.initializeTreeTraversal()
    print("Task 2:", tree.currently_smallest)
    #    node = deepcopy(root)


main()
