from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars =[]
        self.start()
       
        

    def start(self):
        for car in self.all_cars:
            car.hideturtle()
        self.all_cars.clear()
        self.speed = 8
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_cars(self):
        num = random.randint(1,self.speed)
        if num == 1:
            car = Turtle()
            car.shape('square')
            car.shapesize(1,2)
            car.penup()
            pos = random.randint(-250,250)
            car.goto(300,pos)
            col = random.choice(COLORS)
            car.color(col)
            self.all_cars.append(car)

    def move(self):
        for car in self.all_cars:
            car.backward(self.car_speed)
    def level_up(self):
        self.car_speed += MOVE_INCREMENT
        if self.speed != 3: 
            self.speed -=1  
