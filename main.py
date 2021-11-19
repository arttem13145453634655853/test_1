from turtle import *


def cube(n):
    if n <= 10:
        for i in range(4):
            fd(5)
            lt(90)
    else:
        cube(n//2)
        for i in range(4):
            fd(n)
            lt(90)

penup()
setpos(-250,-250)
pendown()
cube(1000)
mainloop()