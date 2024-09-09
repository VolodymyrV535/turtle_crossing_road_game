from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.level = 0
        self.penup()
        self.hideturtle()
        self.level_up()        
        
        
    def level_up(self):
        self.level += 1
        self.clear()
        self.goto(-280, 260)
        self.write(arg=f"Level: {self.level}", font=FONT)
    
    
    def game_over(self):
        self.goto(-75, 0)
        self.write(arg="GAME OVER", font=FONT)
