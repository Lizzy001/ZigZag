import turtle as t
import random

lizzy = t.Turtle()

colours = ["dark red", "coral", "deep pink", "lime", "blue", "cyan"]
directions = [0, 90, 180, 270]
lizzy.pensize(15)
lizzy.speed("slow")

for _ in range(1000):
    lizzy.color(random.choice(colours))
    lizzy.backward(30)
    lizzy.setheading(random.choice(directions))


def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        angle = 360 / num_sides
        lizzy.forward(80)
        lizzy.right(angle)


for shape_side_n in range(3, 10):
    lizzy.color(random.choice(colours))
    draw_shape(shape_side_n)
