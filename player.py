from turtle import Turtle


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.setheading(90)
        self.restart()

    def go_up(self):
        self.forward(MOVE_DISTANCE)
        """below is my own method to move turtle up"""
        # new_y = self.ycor() + MOVE_DISTANCE
        # self.goto(self.xcor(), new_y)

    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
    '''My own method to reach starting position'''
    def restart(self):
        self.goto(STARTING_POSITION)



