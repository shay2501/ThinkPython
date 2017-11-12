import math

def eval_loop():
    while True:
        line = input('> ')
        if line == 'done':
            break
        print(eval(line))

#print('Done!')


def mysqrt( a ):
    x = 3
    while True:
        #print(x)
        y = (x + a/x) / 2
        #print('x = ', x, ' y = ', y)
        if y == x:
            break
        x = y
    return x

def test_square_root():
        a  = 1
        print('a   mysqrt(a)     math.sqrt(a)  diff')

        while a < 10:
            my = mysqrt(a)
            ma = math.sqrt(a)
            #print(my)
            #print(ma)
            print(a, '   ', my, '     ', ma, '  ', my - ma)
            a = a + 1

def factorial(n):
    if(n == 0):
        return 1

    return n * factorial(n-1)

def estimate_pi():
    factor = (2 * math.sqrt(2))/9801
    total = 0
    min = 1e-15
    k=0
    while True:
        num = factorial(4*k) * (1103 + (26390 * k))
        den = factorial(k)** 4 * 396**(4*k)
        term = (num/den) * factor
        total += term
        if(abs(term) < min):
            break
        k+=1
    return 1/total


#test_square_root()
#eval_loop()

print(estimate_pi())
print(math.pi)
