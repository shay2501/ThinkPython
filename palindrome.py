#exercise 6.3
def first(word):
    if(len(word) > 0):
        return word[0]
    return word

def last(word):
    if(len(word) > 0):
        return word[-1]
    return word

def middle(word):
    if(len(word) >= 2):
        return word[1:-1]
    return word

def check_palindrome(word):
    if first(word) == last(word):
        if len(word) > 1:
            check_palindrome(middle(word))
        return 'Yes'
    return 'No'

wrd = 'freref'
print(first(wrd))
print(last(wrd))
print(middle(wrd))
print(check_palindrome(wrd))
