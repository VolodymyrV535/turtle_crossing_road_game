import time
import random

from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("turtle crossing the road")
screen.tracer(0)

# turtle initialization
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.up, "Up")

cars = []

car_creation_iterator = 0

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    car_creation_iterator += 1
       
    if car_creation_iterator % 6 == 0:
        car_manager.create_car()
    
    # move all cars to the left  
    car_manager.move_cars()
    
    # detect colision with the car
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            game_is_on = False
    
            # game over event 
            scoreboard.game_over()            
               
    # detect colision with the top 
    if player.in_the_finish_line():
        # go to new level
        player.reset()
        
        # speed up every car
        car_manager.level_up()
        scoreboard.level_up()     
                            
    screen.update()
    
screen.exitonclick()
