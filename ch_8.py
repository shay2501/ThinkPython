#As an exercise, write a function that takes a string as an argument and displays the letters backward, one per line.

fruit = 'banana'

def backward(fruit):
    index = -1
    stopPt = -1 * len(fruit)

    while index >= stopPt:
        print(fruit[index])
        index -= 1

def find(word, letter, idx):
    index = idx
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1

def count(word, l):
    count = 0
    index = find(word, l, 0)

    while(index != -1):
        count = count + 1
        index = find(word, l, index + 1)
    return count

def is_palindrome(word):
    return word == word[::-1]

def rotate_word(word, shiftamt):
    returnStr = ''
    for l in word:
        c = ord(l)
        c += shiftamt
        returnStr += chr(c)
    return returnStr

wrd = 'banana'
letter = 'n'
backward(fruit)
print(fruit[:])

print(find(wrd, letter, 2))
print(count(wrd, letter))

print(wrd.count('n'))

print(wrd[::-1])

print(is_palindrome('panap'))

print(rotate_word('Dog', -1))
