STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
from turtle import Turtle
import time

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.start()
        
    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def start(self):
        self.shape('turtle')
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def level_up(self):
        if self.ycor() == FINISH_LINE_Y:
            self.goto(STARTING_POSITION)
            time.sleep(0.2)
            return True
        return False