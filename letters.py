import turtle

from ch_4 import circle, arc



def draw_l(t, n):
    t.lt(90)
    t.fd(n)
    t.lt(180)
    t.pu()
    t.fd(n)
    t.lt(90)
    t.pd()
    t.fd(n/2)

def draw_n(t, n):
    t.lt(90)
    t.fd(n)
    t.rt(150)
    t.fd(n * 1.1)
    t.lt(150)
    t.fd(n)
    t.pu()
    t.lt(180)
    t.fd(n)
    t.lt(90)

def draw_m(t, n):
    print('m')
    t.lt(90)
    t.fd(n)
    t.rt(135)
    t.fd(n/2)
    t.lt(90)
    t.fd(n/2)
    t.rt(135)
    t.fd(n)
    #t.pu()
    #t.lt(180)
    #t.fd(n)
    t.lt(90)

def draw_o(t, n):
    print('o')
    t.pu()
    t.fd(n/2)
    t.pd()
    t.lt(20)
    arc(t, n/2, 160)
    t.lt(20)
    arc(t, n/2, 160)
    #t.lt(90)

def draw_p(t, n):
    print('p')
    t.lt(90)
    t.fd(n)
    t.lt(180)
    t.fd(n/2)
    t.rt(90)
    arc(t, n/2, 180)
    t.pu()
    t.lt(180)
    t.fd(n)

def draw_space(t):
    t.pu()
    t.fd(30)
    t.pd()

bob = turtle.Turtle()

draw_l(bob, 100)
draw_space(bob)
draw_n(bob, 100)
draw_space(bob)
draw_m(bob, 100)
draw_space(bob)
draw_o(bob, 100)
draw_space(bob)
draw_p(bob, 100)

turtle.mainloop()
