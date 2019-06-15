import random;

HEIGHT=400
WIDTH=400

rocks = []
lives = 3
ROCK_SPEED = 2

player = Actor("alien")

player.midbottom = (WIDTH/2, HEIGHT)

def update_player():
    global player

    if keyboard.left:
        player.left -= 5

    if keyboard.right:
        player.x += 5

    if player.left < 0:
        player.left = 0

    if player.right > WIDTH:
        player.right = WIDTH

def update_rocks():
    global rocks, rock_speed, lives

    if len(rocks) < 2 and random.randint(0, 40) < 5:
        rock = Actor("rock")
        rock.center = (random.randint(20, WIDTH-20), 0)
        rock.angle = random.randint(0, 360)

        rocks.append(rock)

    rocks_active = []

    for rock in rocks:
        rock.bottom += ROCK_SPEED

        if player.colliderect(rock):
            lives -= 1
            sounds.eep.play()
        else:
            if rock.top < HEIGHT:
                rocks_active.append(rock)

    rocks = rocks_active



def draw_playing():

    player.draw()

    for rock in rocks:
        rock.draw()

def draw_lives():
    global lives
    lives_text = "Lives: "+str(lives)
    screen.draw.text(lives_text, (3,3), color="orange")

def update():
    global lives
    if lives > 0:
        update_player()
        update_rocks()

def draw():

    screen.clear()

    draw_playing()

    draw_lives()

    if lives < 1:
        screen.draw.text("Game Over", center=(WIDTH/2, HEIGHT/2),  fontsize=60, color="red")





