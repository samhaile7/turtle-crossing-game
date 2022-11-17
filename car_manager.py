from turtle import Turtle
import random
import time
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 10
MOVE_INCREMENT = 10
#START_POS = (random.randrange(300,350,10), random.randrange(-200,200, 10))
LANES = [-200, -150, -100, -50, 0, 50, 100, 150, 200]

class CarManager():
    def __init__(self):
        super().__init__()
        self.car_list = []

    def create_car(self):

        new_car = Turtle()
        new_car.penup()
        new_car.hideturtle()
        new_car.goto(random.randrange(250, 1000, 60), random.randrange(-200, 200, 60))
        new_car.shape("square")
        new_car.shapesize(1,2)
        new_car.color(random.choice(COLORS))
        new_car.showturtle()
        self.car_list.append(new_car)




    def move_left(self):
        for all in self.car_list:
            all.backward(MOVE_INCREMENT)







    # def move_left(self):
    #     for i in range(30):
    #         self.forward(MOVE_INCREMENT)
    #

