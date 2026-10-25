FONT = ("Courier", 16, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self, shape = "classic", undobuffersize = 1000, visible = False):
        super().__init__(shape, undobuffersize, visible)
        self.start()
    def level_up(self):
        self.level += 1
        self.display_score()

    def start(self):
        self.level=0
        self.penup()
        self.goto(-230,260)
        self.display_score()
        
    def display_score(self):
        self.clear()
        self.write(f"level - {self.level}",False,'center',FONT)

    def game_over(self):
        self.goto(0,200)
        self.write(f"Game Over , your score is: {self.level}",False,'center',FONT)
