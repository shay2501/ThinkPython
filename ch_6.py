#As an exercise, write a compare function takes two values, x and y, and
#returns 1 if x > y, 0 if x == y, and -1 if x < y.

def value_compare(x, y):
    if(x > y):
        return 1
    elif(x == y):
        return 0
    elif(x < y):
        return -1

def is_between(x, y, z):
    return x <= y <= z

#exercise 2
def ack(m, n):
    if(m == 0):
        return n + 1
    elif(m > 0 and n == 0):
        return ack(m-1, 1)
    elif(m > 0 and n > 0):
        return ack(m-1, ack(m, n-1))

#exercise 4
def is_power(a, b):
    if(a == b):
        return True
    elif (a < b):
        return False
    else:
        return is_power(a//b,b)

#exercise 5
def gcd(a,b):
    if(b == 0):
        return a
    else:
        return gcd(b, a%b)

#print(value_compare(5,5))
#print(value_compare(5,6))
#print(value_compare(6,5))
#print(is_between(4,2,3))

print(ack(3,4))

print(is_power(12, 2))
#print(is_power(9,3))
#print(is_power(25,5))
#print(is_power(72,8))

print(gcd(108, 909))
