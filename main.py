import pyray
from Ball import Ball
from tablero import draw_table
from paddle import Cpu, Player

# Initialization
# --------------------------------------------------------------------------------------
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 450
pyray.init_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Pong by: @user")
pyray.init_audio_device()
pyray.set_target_fps(60)  # Set our game to run at 60 frames-per-second
pelota = Ball()

player = Player(20)
cpu = Cpu(800 - 20 - 25)

# Main game loop
while not pyray.window_should_close():
    # Update
    # ----------------------------------------------------------------------------------
    # TODO: Update your variables here
    pelota.verificar_limites()
    player.move()
    cpu.move(pelota.posy)
    if (pyray.check_collision_circle_rec(pelota.get_ball_position(), pelota.radius, player.get_rec_position())):
        pelota.speedx *= -1
        pelota.play_sound()
    if (pyray.check_collision_circle_rec(pelota.get_ball_position(), pelota.radius, cpu.get_rec_position())):
        pelota.speedx *= -1
        pelota.play_sound()
    #
    # ----------------------------------------------------------------------------------
    # Draw
    # ----------------------------------------------------------------------------------
    pyray.begin_drawing()
    #
    pyray.clear_background(pyray.WHITE)
    draw_table()
    pelota.draw()
    player.draw()
    cpu.draw()
    pelota.draw_score()
    #
    pyray.end_drawing()

# De-Initialization
# --------------------------------------------------------------------------------------
pyray.close_window()  # Close window and OpenGL context
# --------------------------------------------------------------------------------------
