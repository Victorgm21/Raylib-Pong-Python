import pyray


class Ball():
    def __init__(self):
        self.posx = 400
        self.posy = 225
        self.radius = 15
        self.speedx = -5
        self.speedy = 5
        self.color = pyray.WHITE
        self.sound = pyray.load_sound("sound.mp3")
        self.score1 = 0
        self.score2 = 0

    def play_sound(self):
        pyray.play_sound(self.sound)    

    def draw(self):
        self.posx += self.speedx
        self.posy += self.speedy
        pyray.draw_circle(self.posx, self.posy, self.radius, self.color)

    def verificar_limites(self):
        if (self.posx > 800 - self.radius) or (self.posx < 0 + self.radius):
            self.posx = 400
            self.posy = 225
            if self.speedx < 0:
                self.score2 += 1
            else:
                self.score1 += 1
            print(f"El partido va a Jugador {self.score1} - {self.score2} Cpu ")
            self.speedx *= -1
        if (self.posy > 450 - self.radius) or (self.posy < 0 + self.radius):
            self.speedy = self.speedy * -1
            pyray.play_sound(self.sound)

    def get_ball_position(self):
        return pyray.Vector2(self.posx, self.posy)
    
    def draw_score(self):
        pyray.draw_text(f"Jugador: {self.score1}", 50, 50, 20, pyray.WHITE)
        pyray.draw_text(f"CPU: {self.score2}", 600, 50, 20, pyray.WHITE)
