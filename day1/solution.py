f = open('data.txt', 'r')

t = [0]
counter = 0
for line in f:
    if not (line == '\n'):
        t[counter] += int(line)
    else:
        counter += 1
        t.append(0)

print("Part 1:", max(t))

t.sort(reverse=True)
print("Part 2:", t[0] + t[1] + t[2])
