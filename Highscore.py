
class Highscore:
    def __init__(self):
        self.points = 0
        self.name = ""

    def load_points(self, filename):
        load_points = open(filename, "r")
        self.name = load_points.readline()
        self.points = int(load_points.readline())
        load_points.close()

    def save_points(self, filename, name, points):
        self.load_points(filename)
        if self.points < points:
            self.points = points
            save_points = open(filename, "w")
            save_points.writelines(str(name) + "\n")
            save_points.writelines(str(points))
            self.name = name
            save_points.close()
