from turtle import Turtle
starting_position = (0, -280)
move_distance = 10
finish_line = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.go_start()
        self.setheading(90)

    def go_up(self):
        self.forward(move_distance)

    def go_start(self):
        self.goto(starting_position)

    def is_at_finish(self):
       if  self.ycor() > finish_line:
           return True
       else:
           return False
