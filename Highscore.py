
class Highscore:
    def __init__(self):
        self.points = 0
        self.name = ""

    def load_points(self, filename):
        load_points = open(filename, "w+")
        self.name = load_points.readline()
        self.points = load_points.readline()

    def save_points(self, filename, name, points):
        self.load_points(filename)
        if self.points < points:
            self.points = points
            save_points = open(filename, "w")
            save_points.writelines(str(name) + "\n")
            save_points.writelines(str(points))
            self.name = name

h = Highscore()

h.load_points("etr")

print(h.points)
print(h.name)
