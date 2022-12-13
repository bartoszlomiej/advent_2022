filename = 'data.txt'

class Processor:
    def __init__(self):
        self.clock = 1
        self.reg_x = 1
        self.processing = False
        self.total_signal_strength = 0
        self.k = 0
        self.rows = []
        self.rows.append("")
        

    def __addx(self, value):
        self.processing = True if not self.processing else False
        self.reg_x += value if not self.processing else 0
        self.clock += 1
        self.updateScreen()
        self.__evaluateSignalStrength()
        
    def __noop(self):
        self.clock += 1
        self.updateScreen()
        self.__evaluateSignalStrength()

    def __evaluateSignalStrength(self):
        if self.clock == 20 + self.k * 40:
            self.total_signal_strength += self.clock * self.reg_x
            self.k += 1

    def executeOperation(self, operation):
        if len(operation) == 1:
            self.__noop()
        else:
            for i in range(2):
                self.__addx(int(operation[1]))

    def printTotalScore(self):
        print("Task 1:", self.total_signal_strength)

    def updateScreen(self):
        if not (self.clock-1) % 40:
            self.rows.append("")
        else:
            self.addPixel()

    def addPixel(self):
        if abs(((self.clock - 1) % 40) - self.reg_x) <= 1:
            self.rows[-1] += "."
        else:
            self.rows[-1] += "#"

    def printRows(self):
        print("Task 2:")
        for r in self.rows:
            print(r)

        
def main():
    f = open(filename, 'r')
    processor = Processor()
    for line in f:
        t = line.split(" ")
        processor.executeOperation(t)

    processor.printTotalScore()
    processor.printRows()
main()
