import random

WIDTH = 400
HEIGHT = 400
CELL_SIZE = 20
MOVE_RATE = 0.35

playing = True

segment = {
    "x": 2,
    "y": 3
}

apple =  None

snake = {
    "grow_body": False,
    "direction": {
        "x": 1,
        "y": 0
    },
    "body": [segment],
    "next_move": MOVE_RATE
}

def update(ellapsed):
    global playing
    if (playing == True):
        updateApple()
        updatePlaying(ellapsed)
        updateCheckPlaying()


def updateApple():
    global apple, snake

    head = snake["body"][0];

    if(apple is None):
        apple = {
            "x": random.randint(1, WIDTH/CELL_SIZE) - 1,
            "y": random.randint(1, WIDTH/CELL_SIZE) - 1
        }
    else:
        if(head["x"] == apple["x"] and  head["y"] == apple["y"]):
            apple = None
            snake["grow_body"] = True

def updateCheckPlaying():
    global snake, playing

    head = snake["body"][0];

    if(head["x"] < 0 or head["x"] > WIDTH/CELL_SIZE):
        playing = False

    if(head["y"] < 0 or head["y"] > HEIGHT/CELL_SIZE):
        playing = False

    body_count = snake["body"].count(head)
    if(body_count > 1):
        print("Body check dead")
        playing = False

def updatePlaying(ellapsed):

    global snake

    snake["next_move"] = snake["next_move"] - ellapsed;

    if(snake["next_move"] < 0):

        snake["next_move"] = MOVE_RATE

        next_head = {
            "x": snake["body"][0]["x"] + snake["direction"]["x"],
            "y": snake["body"][0]["y"] + snake["direction"]["y"]
        }

        snake["body"].insert(0, next_head)
        if(snake["grow_body"]):
            snake["grow_body"]=False
        else:
            del snake["body"][-1]

    if keyboard.left:
        snake["direction"]["x"] = -1
        snake["direction"]["y"] = 0

    if keyboard.right:
        snake["direction"]["x"] = 1
        snake["direction"]["y"] = 0

    if keyboard.up:
        snake["direction"]["x"] = 0
        snake["direction"]["y"] = -1

    if keyboard.down:
        snake["direction"]["x"] = 0
        snake["direction"]["y"] = 1

def draw():

    if (playing == True):
        drawSnake()
        drawApple()
    else:
        drawGameOver()

def drawApple():

    global apple

    if(apple is not None):
        print(apple)
        apple_color =  255, 0, 0
        box = Rect((apple["x"] * CELL_SIZE,  apple["y"] * CELL_SIZE), (CELL_SIZE, CELL_SIZE))
        screen.draw.filled_rect(box, apple_color)

def drawSnake():
    global snake

    screen.fill((0,0,0))

    for segment in snake["body"]:
        box = Rect((segment["x"] * CELL_SIZE,  segment["y"] * CELL_SIZE), (CELL_SIZE, CELL_SIZE))
        cell_color =  0, 255, 0
        screen.draw.filled_rect(box, cell_color)


def drawGameOver():
    screen.draw.text("Game Over", centerx=WIDTH/2, centery=HEIGHT/2, color="orange", fontsize=64, )

def random_fill():

    for y in range(0, int(HEIGHT / CELL_SIZE)):
        for x in range(0, int(WIDTH / CELL_SIZE)):
            box = Rect((x * CELL_SIZE,  y * CELL_SIZE), (CELL_SIZE, CELL_SIZE))
            cell_color = random.randint(0, 255), random.randint(0, 255), 0
            screen.draw.filled_rect(box, cell_color)