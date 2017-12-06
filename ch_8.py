#As an exercise, write a function that takes a string as an argument and displays the letters backward, one per line.

fruit = 'banana'

def backward(fruit):
    index = -1
    stopPt = -1 * len(fruit)

    while index >= stopPt:
        print(fruit[index])
        index -= 1

backward(fruit)
