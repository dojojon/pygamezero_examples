import random;

HEIGHT=400
WIDTH=400

# Speed the rocks fall
ROCK_SPEED = 2

# List of rocks
rocks = []

# Player lives
lives = 3


# Create a player using the alien image and put at bottom of the screen
player = Actor("alien")
player.midbottom = (WIDTH/2, HEIGHT)

# Update the player and move if the keyboard is pressed
def update_player():
    global player

    # Keyboard input
    if keyboard.left:
        player.left -= 5

    if keyboard.right:
        player.x += 5

    # Prevent player leaving the left/right of screen
    if player.left < 0:
        player.left = 0

    if player.right > WIDTH:
        player.right = WIDTH

# Update the rocks
def update_rocks():
    global rocks, ROCK_SPEED, lives

    # Add new rocks if we have less than 3 and some random number
    if len(rocks) < 3 and random.randint(0, 40) < 5:
        rock = Actor("rock")
        rock.center = (random.randint(20, WIDTH-20), 0)
        rock.angle = random.randint(0, 360)
        # Add new rock to rocks list
        rocks.append(rock)

    # List to contain rocks that are still on the screen
    rocks_active = []

    # Process all the rocks
    for rock in rocks:

        #Move rock down the screen a little bu the
        rock.bottom += ROCK_SPEED

        #Check if the player has hit the rock
        if player.colliderect(rock):
            # The rock hit the player, reduce lives by 1 and play sound
            lives -= 1
            sounds.eep.play()
        else:
            # Rock not hit player and the top of the rock it still on the screen
            if rock.top < HEIGHT:
                # Add rock to the active rock list
                rocks_active.append(rock)

    # Replace the rocks list with the list containing the rocks still on the screen
    rocks = rocks_active


# Draw for when we are still playing
def draw_playing():

    player.draw()

    for rock in rocks:
        rock.draw()

# Draw the lives on the screen
def draw_lives():
    global lives
    lives_text = "Lives: "+str(lives)
    screen.draw.text(lives_text, (3,3), color="orange")

# Update function where we call our other functions
def update():
    global lives

    # Only update the player and rocks if we are alive
    if lives > 0:
        update_player()
        update_rocks()

# Draw function we use to call our draw functions
def draw():

    # Empty the screen
    screen.clear()

    # Call function for the playing objects
    draw_playing()

    # Call function to draw lives
    draw_lives()

    # If we don't have lives, draw game over
    if lives < 1:
        screen.draw.text("Game Over", center=(WIDTH/2, HEIGHT/2),  fontsize=60, color="red")




