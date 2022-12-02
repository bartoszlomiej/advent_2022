f = open('data.txt', 'r')

opponent = {'A': 1, 'B': 2, 'C': 3}
me = {'X': 1, 'Y': 2, 'Z': 3}


def duel_outcome(op_move, my_move):
    if op_move == (my_move + 1) or (op_move == 1 and my_move == 3):
        return 0
    elif op_move == (my_move - 1) or (my_move == 1 and op_move == 3):
        #        print('Won game: ', op_move, my_move)
        return 6
    else:
        return 3


def ultra_top_strategy_guide(op_move, my_move):
    if my_move == 1:
        return op_move - 1 if op_move > 1 else 3
    elif my_move == 2:
        return op_move + 3
    else:
        return (op_move + 1) + 6 if op_move < 3 else 1 + 6


sum_of_point = [0, 0]
for line in f:
    t = line.split(' ')
    op_move = opponent[t[0]]
    my_move = me[t[1][0]]
    sum_of_point[0] += duel_outcome(op_move, my_move) + my_move
    sum_of_point[1] += ultra_top_strategy_guide(op_move, my_move)

print('Part 1:', sum_of_point[0])
print('Part 2:', sum_of_point[1])
