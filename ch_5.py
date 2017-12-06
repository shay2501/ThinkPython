from datetime import datetime, date, time
from time import time
import turtle

#As an exercise, draw a stack diagram for print_n called with s = 'Hello' and n=2.


#Then write a function called do_n that takes a function object and a number, n,
#as arguments, and that calls the given function n times.
#first time I did this I didn't have the IF stmt and I got an infinite recursion error
# anyone else?
def do_n(f, n):
    if(n > 0):
        f()
        do_n(f, n-1)
    else:
        print('All Done!')

def printStuff():
    print('Shannon')


def get_time():
    dt = datetime.now()
    print(dt.strftime("The time is: %H:%M:%S and it has been " + repr(int(time()/86400)) + " days since epoch"))

def check_fermat(a,b,c,n):
    if(n > 2 and (pow(a,n) + pow(b, n) == pow(c,n))):
        print("Holy Cow Fermat was wrong!")
    else:
        print("No that doesn't work")

def do_fermat():
    a = input("Input a value for a to check Fermat's theorem: ")
    b = input("Input a value for b to check Fermat's theorem: ")
    c = input("Input a value for c to check Fermat's theorem: ")
    n = input("Input a value for n to check Fermat's theorem: ")
    check_fermat(int(a), int(b), int(c), int(n))

def is_triangle(a,b,c):
    result = 'Yes'
    if(a+b < c):
        result = 'No'
    if(c+b < a):
        result = 'No'
    if(a+c < b):
        result = 'No'
    print(result)

def check_triangle():
    a = input("Enter side a of triangle: ")
    b = input("Enter side b of triangle: ")
    c = input("Enter side c of triangle: ")
    is_triangle(int(a), int(b), int(c))

def draw(t, length, n):
    if n == 0:
        return
    angle = 50
    t.fd(length*n)
    t.lt(angle)
    draw(t, length, n-1)
    t.rt(2*angle)
    draw(t, length, n-1)
    t.lt(angle)
    t.bk(length*n)

def recurse(n, s):
    if n == 0:
        print(s)
    else:
        recurse(n-1, n+s)

def koch(t, l):
    angle = 60
    d = 3
    if l < 3:
        t.fd(l)

    else:
         koch(t, l/d)
         t.lt(angle)
         koch(t,l/d)
         t.rt(angle * 2)
         koch(t,l/d)
         t.lt(angle)
         koch(t,l/d)

recurse(3, 0)

do_n(printStuff, 10)
get_time()
#do_fermat()
#check_triangle()
bob = turtle.Turtle()
#draw(bob, 5, 15)
koch(bob, 100)
turtle.mainloop()
