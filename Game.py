import random
import time
import turtle

from Shape import Shape
from Text import Text


class Game:
    def __init__(self):
        self.window = turtle.Screen()
        self.window.bgcolor("white")
        self.window.title("Catch the Circles!")
        self.window.tracer(0)

        self.shapes = []
        self.scores = 0
        self.start_time = time.time()
        self.duration = 30
        self.score_text = Text(-200, 250, f"Score: {self.scores}")
        self.timer_text = Text(200, 250, f"Duration: {self.duration}")

    def create_shapes(self):
        x = random.randint(-250, 250)
        y = 250
        shape = random.choice(["circle", "square", "triangle"])
        color = random.choice(["red", "blue", "turquoise", "Dark blue", "purple"])
        new_shape = Shape(x, y, shape, color)
        new_shape.show()
        self.shapes.append(new_shape)

    def move_shapes(self):
        for i in self.shapes:
            i.move()

            if i.shape.ycor() < -250:
                self.shapes.remove(i)
                i.hide()


    def on_shape_click(self, x, y):
        for shape in self.shapes:
            if shape.shape.distance(x, y) < 40 and shape.shape.shape() == "circle":
                self.shapes.remove(shape)
                shape.hide()
                self.scores += 1
            elif shape.shape.distance(x, y) < 40 and shape.shape.shape() != "circle":
                self.shapes.remove(shape)
                shape.hide()
                self.scores -= 1

            self.score_text.write_text(f"Score: {self.scores}")

    def update_timer(self):
        time_passed = int(time.time() - self.start_time)
        time_left = max(0, self.duration - time_passed)
        self.timer_text.write_text(f"Time: {time_left}")
        return time_left >0

    def start(self):
        self.window.listen()
        self.window.onclick(self.on_shape_click)

        while self.update_timer():
            self.window.update()
            self.create_shapes()
            self.move_shapes()
            time.sleep(0.1)

        self.window.textinput("Game over!", f"Highest Score: {self.scores}")
