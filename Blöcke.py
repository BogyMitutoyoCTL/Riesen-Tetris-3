class Testrisblock:
    def __init__(self, alphalist):
        self.color=(100,0,20)
        self.posotion=(3,5)
        self.orientations=alphalist
        self.orientation=0

    def showme(self):
        templist=self.orientations[0]
        for row in templist:
            for colum in row:
                if colum ==1:
                    print("x",end="")
                else:
                    print(" ",end="")
            print()

list1=[[1,1,0,],[0,1,0,],[0,1,0]]
list2=[[0,0,0],[1,1,1],[1,0,0]]
list3=[[0,1,0],[0,1,0],[0,1,1]]
list4=[[1,0,0],[1,1,1],[0,0,0]]
alphalist=[list1,list2,list3,list4]
L=Testrisblock(alphalist)
L.showme()

