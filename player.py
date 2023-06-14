from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.setheading(90)
        self.go_to_start()
        self.move_y = 5

    def reset_pos(self):
        print("Winner")
        self.setpos(0, -280)

    def move(self):
        new_y = self.ycor() + self.move_y
        self.sety(new_y)

    def is_at_finish(self):
        if self.ycor() == 300:
            return True

    def go_to_start(self):
        self.setpos(0, -280)
