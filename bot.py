import turtle
import random
import time

# Create a screen
screen = turtle.Screen()
screen.title("SNAKE GAME")
screen.setup(width=700, height=700)
screen.tracer(0)
screen.bgcolor("#1d1d1d")

# Creating border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.penup()
border_pen.color("red")
border_pen.pensize(4)
border_pen.goto(-310, 250)
border_pen.pendown()
for _ in range(2):
    border_pen.forward(600)
    border_pen.right(90)
    border_pen.forward(500)
    border_pen.right(90)
border_pen.hideturtle()

# Score
score = 0
delay = 0.1

# Snake
snake = turtle.Turtle()
snake.speed(0)
snake.shape("square")
snake.color("green")
snake.penup()
snake.goto(0, 0)
snake.direction = "stop"

# Food
fruit = turtle.Turtle()
fruit.speed(0)
fruit.shape("square")
fruit.color("white")
fruit.penup()
fruit.goto(0, 100)

# Scoring
scoring = turtle.Turtle()
scoring.speed(0)
scoring.color("white")
scoring.penup()
scoring.hideturtle()
scoring.goto(0, 300)
scoring.write("Score: {}".format(score), align="center", font=("Courier", 24, "bold"))


# Functions to move the snake
def snake_go_up():
    if snake.direction != "down":
        snake.direction = "up"

def snake_go_down():
    if snake.direction != "up":
        snake.direction = "down"

def snake_go_left():
    if snake.direction != "right":
        snake.direction = "left"

def snake_go_right():
    if snake.direction != "left":
        snake.direction = "right"

# Keyboard bindings
screen.listen()
screen.onkeypress(snake_go_up, "Up")
screen.onkeypress(snake_go_down, "Down")
screen.onkeypress(snake_go_left, "Left")
screen.onkeypress(snake_go_right, "Right")

# Main game loop
while True:
    screen.update()

    # Move the snake
    if snake.direction == "up":
        y = snake.ycor()
        snake.sety(y + 20)
    elif snake.direction == "down":
        y = snake.ycor()
        snake.sety(y - 20)
    elif snake.direction == "left":
        x = snake.xcor()
        snake.setx(x - 20)
    elif snake.direction == "right":
        x = snake.xcor()
        snake.setx(x + 20)

    # Snake & fruit collision
    if snake.distance(fruit) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        fruit.goto(x, y)
        score += 1
        scoring.clear()
        scoring.write("Score: {}".format(score), align="center", font=("Courier", 24, "bold"))

    time.sleep(delay)

# Keep the window open
turtle.mainloop()
