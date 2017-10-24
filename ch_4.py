import turtle
import math

bob = turtle.Turtle()
print(bob)

def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)

def polyline(t, length, n, angle):

    print("polyline t: ", t)
    print("polyline length: ", length)
    print("polyline n: ", n)
    print("polyline angle: ", angle)
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def polygon(t, length, n):
    polyline(t, length, n, 360/n)

def circle(t, r):
    print("circle t: ", t)
    print("circle r: ", r)
    arc(t, r, 360)

def arc(t, r, angle):
    print("arc t: ", t)
    print("arc r: ", r)
    print("arc angle: ", angle)
    c = 2 * 3.14 * r
    n = int(c/3) + 1

    print("arc c: ", c)
    print("arc n: ", n)
    polyline(t, c/n, n, angle/n )

#exercise 4.3.1 and 4.3.2
#square(bob, 200)

#exercise 4.3.3
#polygon(bob, 50, 7)

#exercise 4.3.4
print("Module: ", bob)
circle(bob, 100)

#exercise 4.3.5
#arc(bob, 50, 300)

turtle.mainloop()
