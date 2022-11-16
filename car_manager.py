from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
START_POS = (random.randrange(300,350,10), random.randrange(-200,200, 10))


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(START_POS)
        self.shape("square")
        self.shapesize(2, 1)
        self.color(random.choice(COLORS))
        self.showturtle()
        self.setheading(180)


        self.move_left()

    def move_left(self):
        self.move_left(MOVE_INCREMENT)


