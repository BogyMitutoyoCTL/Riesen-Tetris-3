class Testrisblock:
    def __init__(self, alphalist):
        self.color = (100, 0, 20)
        self.posotion = (3, 5)
        self.orientations = alphalist
        self.orientation = 0

    def showme(self):
        templist = self.orientations[self.orientation]
        for row in templist:
            for colum in row:
                if colum == 1:
                    print("x", end="")
                else:
                    print(" ", end="")
            print()
        print()
    def turnright(self):
        self.orientation +=1
        if self.orientation == 4:
            self.orientation = 0
    def turnleft(self):
        self.orientation -=1
        if self.orientation == 0:
            self.orientation = 3



list1 = [[1, 1, 0, ], [0, 1, 0, ], [0, 1, 0]]
list2 = [[0, 0, 0], [1, 1, 1], [1, 0, 0]]
list3 = [[0, 1, 0], [0, 1, 0], [0, 1, 1]]
list4 = [[0, 0, 1], [1, 1, 1], [0, 0, 0]]
alphalist = [list1, list2, list3, list4]
L = Testrisblock(alphalist)
L.showme()
L.turnright()
L.showme()
L.turnright()
L.showme()
for Test in range(0,11):
    L.turnright()
    L.showme()