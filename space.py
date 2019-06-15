WIDTH = 400
HEIGHT = 400

MOVE_RATE = 0.15

player = Actor("spaceship")
player.pos = 300, 200

animate(player, pos=(WIDTH/2,HEIGHT/2), tween="decelerate", duration=0.5)

def draw():
    screen.clear()
    player.draw()