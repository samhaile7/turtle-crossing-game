from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 10
MOVE_INCREMENT = 10
#START_POS = (random.randrange(300,350,10), random.randrange(-200,200, 10))


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.car_list = []




    def create_new_car(self):
        x_pos = 300
        car = CarManager()
        car.penup()
        car.hideturtle()
        car.goto(x_pos, random.randrange(-200,200, 40))
        x_pos += 10
        car.shape("square")
        car.shapesize(1, 2)
        car.color(random.choice(COLORS))
        car.showturtle()
        car.setheading(180)
        car.move_left()
        self.car_list.append(car)



    def move_left(self):
        self.forward(MOVE_INCREMENT)


