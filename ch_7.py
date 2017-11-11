import math

while True:
    line = input('> ')
    if line == 'done':
        break
    print(line)

print('Done!')


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

test_square_root()

#print(mysqrt(1))
