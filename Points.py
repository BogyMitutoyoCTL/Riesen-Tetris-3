class Points:
    def __init__(self):
        self.points = 0

    def lines(self, i):
        if i == 1:
            self.points = self.points + 40
        if i == 2:
            self.points = self.points + 100
        if i == 3:
            self.points = self.points + 300
        if i == 4:
            self.points = self.points + 1200

    def traversed_lines(self, y):
        if y > 0:
            self.points = self.points + y


points = Points()
points.lines(4)
points.traversed_lines(8)
print(points.points)