import random

WIDTH = 800
HEIGHT = 400
GRAVITY = .025
FREQUENCY = .15

emit_time = 0

particles = []

def update(elapsed):
    global particles, emit_time, FREQUENCY, GRAVITY
    emit_time = emit_time - elapsed
    if(emit_time < 0):
        emit_time = FREQUENCY

        count = 50
        while(count > 0):
            particle = {
                "vx":  random.uniform(-2, 2),
                "vy":  random.uniform(-3, 3),
                "x":  WIDTH/2,
                "y":  HEIGHT/2,
                "color": (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            }
            particles.append(particle)
            count = count - 1

    alive_particles = []
    kill_count = 0

    for particle in particles:

        particle["vy"] += GRAVITY
        particle["x"] += particle["vx"]
        particle["y"] += particle["vy"]

        if(particle["x"] > 0 and particle["x"] < WIDTH and particle["y"] > 0 and particle["y"] < HEIGHT):
            alive_particles.append(particle)
        else:
            kill_count += 1

    particles = alive_particles

    print("kill count" + str(kill_count))
    print(len(particles))

def draw():
    global particles
    screen.clear()
    for particle in particles:
        position = particle["x"], particle["y"]
        color = particle["color"]
        screen.draw.filled_circle(position, 2, color)