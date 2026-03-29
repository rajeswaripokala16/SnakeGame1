import turtle
import time
import random

# Game configuration
delay = 0.08
score = 0
high_score = 0

# Screen setup
wn = turtle.Screen()
wn.title("🐍 Snake Game - Effective Edition")
wn.bgcolor("light blue")
wn.setup(width=600, height=600)
wn.tracer(0)

# Snake head setup
head = turtle.Turtle()
head.shape("square")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Food setup
food = turtle.Turtle()
food.speed(0)
food.shape(random.choice(['square', 'triangle', 'circle']))
food.color(random.choice(['red', 'green', 'black']))
food.penup()
food.goto(0, 100)

segments = []

# Scoreboard setup
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write("Score: 0  High Score: 0", align="center", font=("candara", 24, "bold"))

# Game functions
def update_score():
    pen.clear()
    pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("candara", 24, "bold"))

def up():
    if head.direction != "down":
        head.direction = "up"

def down():
    if head.direction != "up":
        head.direction = "down"

def left():
    if head.direction != "right":
        head.direction = "left"

def right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        head.sety(head.ycor() + 20)
    if head.direction == "down":
        head.sety(head.ycor() - 20)
    if head.direction == "left":
        head.setx(head.xcor() - 20)
    if head.direction == "right":
        head.setx(head.xcor() + 20)

def quit_game():
    wn.bye()

# Keyboard bindings
wn.listen()
wn.onkeypress(up, "Up")
wn.onkeypress(down, "Down")
wn.onkeypress(left, "Left")
wn.onkeypress(right, "Right")
wn.onkeypress(quit_game, "Escape")

# Main game loop
def game_loop():
    global delay, score, high_score

    wn.update()

    # Check for border collision
    if (head.xcor() > 290 or head.xcor() < -290 
        or head.ycor() > 290 or head.ycor() < -290):
        time.sleep(0.5)
        head.goto(0, 0)
        head.direction = "stop"
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()
        score = 0
        delay = 0.08
        update_score()

    # Check for food collision
    if head.distance(food) < 20:
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        food.goto(x, y)
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("orange")
        new_segment.penup()
        segments.append(new_segment)
        delay = max(0.03, delay - 0.001)
        score += 10
        if score > high_score:
            high_score = score
        update_score()

    # Move snake body
    for i in range(len(segments) - 1, 0, -1):
        x = segments[i-1].xcor()
        y = segments[i-1].ycor()
        segments[i].goto(x, y)
    if len(segments) > 0:
        segments[0].goto(head.xcor(), head.ycor())
    move()

    # Check for self-collision
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(0.5)
            head.goto(0, 0)
            head.direction = "stop"
            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()
            score = 0
            delay = 0.08
            update_score()
            break

    wn.ontimer(game_loop, int(delay * 1000))

# Start the game loop
game_loop()
wn.mainloop()
