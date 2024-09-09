from turtle import Turtle

import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
          
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        
    
    def create_car(self):
        new_car = Turtle("square")
        new_car.color(random.choice(COLORS))
        new_car.shapesize(1, 2)
        new_car.penup()
        random_y = random.choice(range(-250, 270, 20))
        new_car.goto(310, random_y)  #     
        new_car.setheading(180)
        
        self.all_cars.append(new_car)
        
        
    def move_cars(self):
        
        for car in self.all_cars:
            car.forward(self.car_speed)                     


    def level_up(self):
        self.car_speed += MOVE_INCREMENT   
