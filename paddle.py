import pyray


class Paddle():
    def __init__(self, border_distance):
        self.speed = 7
        self.x = border_distance
        self.y = 225 - 60
        self.width = 25
        self.heigh = 120

    def draw(self):
        pyray.draw_rectangle_rounded(
            self.get_rec_position(), 0.8, 0, pyray.WHITE)

    def get_rec_position(self):
        return pyray.Rectangle(self.x, self.y, self.width, self.heigh)


class Player(Paddle):
    def move(self):
        if (pyray.is_key_down(pyray.KEY_W) and self.y > 0):
            self.y -= self.speed
        if (pyray.is_key_down(pyray.KEY_S) and self.y + self.heigh < 450):
            self.y += self.speed


class Cpu(Paddle):
    def move(self, y_ball):
        if (y_ball < self.y + self.heigh / 2) and (self.y > 0):
            self.y -= self.speed
        if (y_ball > self.y + self.heigh / 2) and (self.y + self.heigh < 450):
            self.y += self.speed
