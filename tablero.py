import pyray

verde_claro = pyray.Color(62, 237, 91, 255)

verde_oscuro = pyray.Color(58, 220, 85, 255)


def draw_table():
    for i in range(0, 10):
      if i % 2 == 0:
          pyray.draw_rectangle(80 * i, 0, 80, 450, verde_oscuro)
      else:
          pyray.draw_rectangle(80 * i, 0, 80, 450, verde_claro)
    pyray.draw_line(400, 0, 400, 450, pyray.WHITE)
    pyray.draw_circle_lines(400, 225, 50, pyray.WHITE)
