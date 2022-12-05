from collections import deque

filename = 'data.txt'

def finalWord(stacks, task_id):
    word = ""
    for i in stacks:
        if i:
            word += i.pop()
    print('Task', task_id, ':', word)

def allMoves(moves, stacks):
    while moves:
        makeMove(moves.pop(), stacks)

def makeMove(move, stacks):
    for i in range(move['m']):
        if stacks[move["f"]-1]:
            element_to_move = stacks[move["f"]-1].pop()
            stacks[move['t']-1].append(element_to_move)

def readStacks(line, stacks):
    counter = 0
    for i in line:
        if i != "*" and i != "\n":
            stacks[counter].appendleft(i)
        counter += 1

def checkTwoDigitMove(line, i):
    if line[i] == 'm':
        if line[i+2].isdigit():
            return int(line[i+1]) * 10 + int(line[i+2])
    return int(line[i+1])
        
def readMove(line, moves):
    move = {'m': 0, 'f': 0, 't': 0}
    for i in range(len(line)-1):
        if line[i] in move.keys():
            move[line[i]] = checkTwoDigitMove(line, i)
    moves.appendleft(move)

def readAllData(filename, stacks, moves):
    f = open(filename, 'r')
    for line in f:
        if line[0] == 'm':
            readMove(line, moves)
        else:
            readStacks(line, stacks)
    return moves, stacks

def createStacks():
    stacks = []
    for i in range(9):
        stacks.append(deque())
    return stacks

def main_task_1():
    stacks = createStacks()
    moves = deque()
    moves, stacks = readAllData(filename, stacks, moves)
    for i in stacks:
        print("initial config:", i)
    allMoves(moves, stacks)
    finalWord(stacks, 1)

def allMoves_t2(moves, stacks):
    while moves:
        makeMove_t2(moves.pop(), stacks)

def makeMove_t2(move, stacks):
    buffer_q = deque()
    for i in range(move['m']):
        if stacks[move["f"]-1]:
            buffer_q.append(stacks[move["f"]-1].pop())
    while(buffer_q):
        stacks[move['t']-1].append(buffer_q.pop())
    
def main_task_2():
    stacks = createStacks()
    moves = deque()
    moves, stacks = readAllData(filename, stacks, moves)
    allMoves_t2(moves, stacks)
    finalWord(stacks, 2)
    
main_task_1()
main_task_2()
