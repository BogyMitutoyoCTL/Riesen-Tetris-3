from LED_Matrix_Maler import Painter
from Sound import Sound


class Highscore:
    def __init__(self, filename, leonardo: Painter, sounds: Sound):
        self.points = 0
        self.name = ""
        self.filename = filename
        self.sounds = sounds
        self.leonardo = leonardo
        self.load_points()

    def handle_highscore(self, name, points):
        if points > self.points:
            self.sounds.new_highscore()
            self.save_points(name, points)

        self.leonardo.write_text("HS:" + str(self.points))

    def load_points(self):
        load_points = open(self.filename, "r")

        temp_name = load_points.readline()
        temp_points = load_points.readline()
        load_points.close()

        if len(temp_name) > 0:
            self.name = temp_name

        if len(temp_points) > 0:
            self.points = int(temp_points)

    def save_points(self, name, points: int):
        self.points = points
        self.name = name

        save_points = open(self.filename, "w+")
        save_points.writelines(str(name) + "\n")
        save_points.writelines(str(points))
        save_points.close()


if __name__ == "__main__":
    h = Highscore("highscore.txt", None, None)

    print(h.points)
    print(h.name)

