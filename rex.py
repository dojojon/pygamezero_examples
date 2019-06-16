import pgzrun
import pgzero
import random

WIDTH = 600
HEIGHT = 300
GRAVITY = .25
GROUND = HEIGHT - 32

score = 0

run_speed = 3

ground = []
rocks = []

player = Actor("dino-1")
player.midbottom = (64, GROUND)
player.isJumping = False
player.v = 0
player.alive = True

player_frame = 0


ground_left = 0
while ground_left < WIDTH + 64:
    ground_block = Actor("sand")
    ground_block.top = HEIGHT - ground_block.height
    ground_block.left = ground_left
    ground_left += ground_block.width
    ground.append(ground_block)

def update_player():
    if keyboard.space and not player.isJumping:
        player.isJumping = True
        player.v = -8

    if player.isJumping:

        player.v += GRAVITY
        player.bottom += player.v

        if player.bottom > GROUND:
            player.isJumping = False
            player.bottom = GROUND

        if player.top < 0:
            player.top = 0

def update_player_animation():
    global player_frame

    if player.isJumping:
        player.image = "dino-1"
    elif player_frame == 2:
        player.image = "dino-3"
        player_frame = 3
    else:
        player.image = "dino-2"
        player_frame = 2

def update_rocks():
    global rocks, run_speed

    if len(rocks)==0:
        rock = Actor("cactus", bottomleft=(WIDTH - 20, GROUND))
        rocks.append(rock)
    on_screen = []
    for rock in rocks:
        rock.left -= run_speed

        if player.colliderect(rock):
            player.alive = False

        if rock.right > 0:
            on_screen.append(rock)
        else:
            run_speed += 1

    rocks = on_screen

def update_ground():

    first_block = ground[0]
    if first_block.right < 0:
        ground.remove(first_block)
        last_block = ground[-1]
        first_block.left = last_block.right
        ground.append(first_block);


    for ground_block in ground:
        ground_block.left -= run_speed


def update():
    global score
    if player.alive:
        score +=1
        update_player()
        update_rocks()
        update_ground()

def draw():

    screen.fill((0, 10, 23))

    player.draw()
    screen.draw.text(str(score), (20,20))

    for rock in rocks:
        rock.draw()

    for ground_block in ground:
        ground_block.draw()

clock.schedule_interval(update_player_animation, .25)

pgzrun.go()