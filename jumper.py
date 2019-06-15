import random

HEIGHT = 640
WIDTH = 480

CHUTE_MAX_VELOCITY = 25
GRAVITY = 3

WAVE_FRAME_RATE = .25
wave_next_frame = 0

wind_speed = random.randrange(-5, 5)

print("wind_speed" + str(wind_speed))

player_velocity = {
    "x": 0,
    "y": 0
}

target_position = random.randint(5 * 32, (480) - (5 * 32))
is_chute_open = False
is_chute_cut = False
has_chute_opened = False

player = Actor("jumper", midbottom=(HEIGHT/2, 0))
chute = Actor("chute", midbottom=(HEIGHT/2, - 24))
target = Actor("target", bottomleft=(target_position, HEIGHT - 32))

clouds = []

c = 0
while(c < 6):
    cloud = Actor("cloud", center=(random.randint(-100, WIDTH + 100), (c + 2) * 64))
    clouds.append(cloud)
    c += 1

def update(ellapsed):

    global has_chute_opened, is_chute_open, is_chute_cut, wave_next_frame

    if keyboard.s and has_chute_opened is False:
        is_chute_open = True
        has_chute_opened = True

    if keyboard.d and has_chute_opened is True and is_chute_open is True:
        is_chute_open = False
        is_chute_cut = True

    if player.bottom < HEIGHT - 32:

        player_velocity["y"] += GRAVITY

        if is_chute_open and player_velocity["y"] > CHUTE_MAX_VELOCITY:
            player_velocity["y"] = CHUTE_MAX_VELOCITY

        player_velocity["x"] += ellapsed * wind_speed

        player.y += ellapsed * player_velocity["y"]
        player.x += ellapsed * player_velocity["x"]

    else:

        is_chute_open = False

        if player_velocity["y"] > 100:
            player.image = "jumper_splat"
        else:
            print("wave")
            wave_next_frame -= ellapsed
            print(wave_next_frame)
            if wave_next_frame < 0:
                wave_next_frame = WAVE_FRAME_RATE

                if player.image == "jumper_wave":
                    player.image = "jumper"
                else:
                    player.image = "jumper_wave"

    if(is_chute_open and is_chute_cut is False):
        chute.x = player.x
        chute.y = player.y - 24
    else:
        chute.y += ellapsed * 10
        chute.x += ellapsed * 30

    for cloud in clouds:
        cloud.x += ellapsed * wind_speed * 5
        if cloud.right < 0:
            cloud.left = WIDTH


def draw():

    screen.fill((135, 206, 235))

    drawGround()

    for cloud in clouds:
        cloud.draw()

    if is_chute_open or is_chute_cut:
        chute.draw()

    target.draw()

    player.draw()


def drawGround():

    rect = Rect((0, HEIGHT - 32), (32 * 20, 32))
    color = (20, 200, 20)
    screen.draw.filled_rect(rect, color)