import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
cars = CarManager()
score = Scoreboard()

def listen():
    screen.listen()
    screen.onkeypress(player.move_up,'Up')
    screen.onkeypress(player.move_up,'w')
listen()

def restart_game():
    player.start()
    cars.start()
    score.start()
    listen()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_cars()
    cars.move()
    if player.level_up():
        cars.level_up()
        score.level_up()

    #collision with cars
    for car in cars.all_cars:
        if player.distance(car) < 20:
            score.game_over()
            while True:
                res = screen.textinput('Game Over','DO you want to Try Again ?(yes/no) :  ')
                if res.lower() == 'yes':
                    game_is_on = True
                    restart_game()
                    break
                elif res.lower() == 'no' or res.lower() == None:
                    game_is_on = False
                    break
                else:
                    continue
            break

screen.exitonclick()