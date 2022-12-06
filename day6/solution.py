from collections import deque

filename = 'data.txt'


def createCharBuffer(line, n_chars):
    char_buffer = deque()
    for i in range(n_chars):
        char_buffer.appendleft(line[i])
    return char_buffer


def areDuplicatesInDeque(char_buffer):
    if len(set(char_buffer)) == len(char_buffer):
        return False
    return True


def findFourDiffChar(line, char_buffer, n_chars):
    counter = n_chars + 1
    for char in range(n_chars, len(line)):
        if not line[char] in char_buffer and not areDuplicatesInDeque(
                char_buffer):
            return counter
        counter += 1
        char_buffer.pop()
        char_buffer.appendleft(line[char])


def main():
    f = open(filename, 'r')
    for line in f:
        char_buffer = createCharBuffer(line, 3)
        print("Task 1:", findFourDiffChar(line, char_buffer, 3))
        char_buffer = createCharBuffer(line, 13)
        print("Task 2:", findFourDiffChar(line, char_buffer, 13))


main()
