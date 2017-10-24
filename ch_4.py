import turtle
import math

#bob = turtle.Turtle()
#print(bob)

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
    """t is Turtle, r is int, and angle is int """
    print("arc t: ", t)
    print("arc r: ", r)
    print("arc angle: ", angle)
    #arc length
    c = 2 * math.pi * r * abs(angle)/360

    #number of sides
    n = int(c/3) + 1

    print("arc c: ", c)
    print("arc n: ", n)

    #c/n is step length
    step_angle = float(angle)/n

     # making a slight left turn before starting reduces
    # the error caused by the linear approximation of the arc
    t.lt(step_angle/2)
    polyline(t, c/n, n, step_angle)
    t.rt(step_angle/2)

def petal(t, r, angle):
    """Draws a petal using two arcs.

    t: Turtle
    r: radius of the arcs
    angle: angle (degrees) that subtends the arcs
    """
    for i in range(2):
        arc(t, r, angle)
        t.lt(180-angle)

def flower(t,r, angle, n):
    for i in range(n):
        petal(t, r, angle)
        bob.rt(360/n)

def pie(t, length, n):
    for i in range(n):
        polygon(t, length, 3)
        t.rt(360/n)

def polypie(t, length, n):
    angle = 360.0/n

    #draw the specified number of triangles
    for i in range(n):
        triangle(t, length, angle/2)
        t.lt(angle)

def triangle(t, r, angle):
    y = r * math.sin(angle * math.pi / 180)

    t.rt(angle)
    t.fd(r)
    t.lt(90+angle)
    t.fd(2*y)
    t.lt(90+angle)
    t.fd(r)
    t.lt(180-angle)

#exercise 4.3.1 and 4.3.2
#square(bob, 200)

#exercise 4.3.3
#polygon(bob, 50, 7)

#Exercise 4.12.1 - stack diagram
#print("Module: ", bob)
#exercise 4.3.4
#circle(bob, 100)

#exercise 4.3.5
#arc(bob, 50, 300)

#exercise 4.12.2
#flower(bob, 200, 60, 7)
#flower(bob, 200, 70, 10)
#flower(bob, 200, 30, 20)

#exercise 4.12.3
#pie(bob, 100, 6)
#polypie(bob, 100, 10)


#turtle.mainloop()
