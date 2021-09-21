import turtle
from random import randint
from time import sleep

body_parts = []

# creation of the game bored
wn = turtle.Screen()
wn.listen()
wn.bgcolor("Black")
wn.setup(700, 700)
wn.title("Snake Game G.K.C")
wn.tracer(0)

# Snake head object
head = turtle.Turtle("square")
head.color("Green")
head.speed(0)
head.penup()
head.direction = "stop"

# fruit object
fruit = turtle.Turtle("square")
fruit.speed(0)
fruit.shapesize(0.6)
fruit.color("red")
fruit.penup()
fruit.goto(80, 50)

# Writing score and High score
Writer = turtle.Turtle()
scores = [0, 0]
Writer.color("White")

Writer.penup()
Writer.hideturtle()
Writer.speed(0)

Writer.goto(-100, 300)
Writer.write(f"Score : {scores[0]}", align="right", font=("Comic Sans MS", 15, "normal"))

Writer.goto(100, 300)
Writer.write(f"High Score : {scores[1]}", align="left", font=("Comic Sans MS"
, 15, "normal"))

# Direction functions
def go_up():
    if head.direction != "down":
        head.direction = "up"
def go_down():
    if head.direction != "up":
        head.direction = "down"
def go_right():
    if head.direction != "left":
        head.direction = "right"
def go_left():
    if head.direction != "right":
        head.direction = "left"

# move function
def move():
    forward_with_pixels = 20
    if head.direction == "up":
        head.sety(head.ycor() + forward_with_pixels)

    if head.direction == "down":
        head.sety(head.ycor() - forward_with_pixels)

    if head.direction == "right":
        head.setx(head.xcor() + forward_with_pixels)

    if head.direction == "left":
        head.setx(head.xcor() - forward_with_pixels)

wn.onkey(go_up, "Up")
wn.onkey(go_down, "Down")
wn.onkey(go_right, "Right")
wn.onkey(go_left, "Left")

def scoring():
    if head.distance(fruit) < 16:
        Writer.clear()
        scores[0] += 10
        fruit.goto(randint(-335, 335), randint(-335, 335))
        if scores[1] < scores[0]:
            scores[1] = scores[0]

        Writer.goto(-100, 300)
        Writer.write(f"Score : {scores[0]}", align="right", font=("Comic Sans MS", 15, "normal"))

        Writer.goto(100, 300)
        Writer.write(f"High Score : {scores[1]}", align="left", font=("Comic Sans MS" , 15, "normal"))

        New_turtle = turtle.Turtle()
        New_turtle.penup()
        New_turtle.color("Red")
        New_turtle.shape("square")
        New_turtle.speed(0)
        body_parts.append(New_turtle)

        # print(body_parts)

def border_collision():
    if head.xcor() > 340 or head.xcor() < -340 or head.ycor() < -340 or head.ycor() > 340:
        sleep(0.5)
        scores[0] = 0
        Writer.clear()
        head.direction = "stop"
        head.goto(0, 0)
        scores[1] == scores[1]

        Writer.goto(-100, 300)
        Writer.write(f"Score : {scores[0]}", align="right", font=("Comic Sans MS", 15, "normal"))

        Writer.goto(100, 300)
        Writer.write(f"High Score : {scores[1]}", align="left", font=("Comic Sans MS" , 15, "normal"))

        if len(body_parts) > 0:
            body_parts[-1].forward(100)

        body_parts.clear()







def snake_body():
    last_index = len(body_parts) - 1

    for i in range(last_index,0, -1):
        x = body_parts[i - 1].xcor()
        y = body_parts[i - 1].ycor()
        body_parts[i].goto(x, y)

    if len(body_parts) > 0:
        body_parts[0].goto(head.xcor(), head.ycor())


# game main loop
while True:
    wn.update()
    sleep(0.1)
    scoring()
    snake_body()
    move()
    border_collision()
