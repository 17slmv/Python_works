from turtle import Turtle
import random
colors = ["red", "purple", "green", "blue", "green", "yellow"]
starting_move_distance = 5
move_increment = 10

class CarManager(Turtle):
    def __init__(self):
        self.all_cars = []
        self.speed_car = starting_move_distance

    def create_car(self):
        rand = random.randint(1,6)
        if rand == 1:
            new_car  = Turtle("square")
            new_car.shapesize(1,2)
            new_car.penup()
            new_car.color(random.choice(colors))
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def cars_move(self):
        for car in self.all_cars:
            car.backward(self.speed_car)
    def level_up(self):
        self.speed_car += move_increment



