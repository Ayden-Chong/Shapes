import turtle


class Text:
    def __init__(self, x, y, text):
        self.pen = turtle.Turtle()
        self.pen.hideturtle()
        self.pen.penup()
        self.pen.speed(0)
        self.pen.goto(x, y)
        self.pen.color("black")
        self.write_text(text)

    def write_text(self, text):
        self.pen.clear()
        self.pen.write(text, align="center", font=("Arial", 19, "normal"))
