
from ch_8 import is_palindrome

def words_over_20(filename):
    fin = open(filename)
    ln = fin.readline()
    while len(ln) > 0:
        if len(ln.strip()) >= 20:
            print(ln.strip())
        ln = fin.readline()

def words_without_e(filename):
    fin = open(filename)
    ln = fin.readline()
    while len(ln) > 0:
        if has_no_e(ln.strip()):
            print(ln.strip())
        ln = fin.readline()

def has_no_e (word):
    for c in word:
        if c == 'e':
            return False
    return True

def avoids(word, list):
    foundlist  = ''
    for l in list:
        if word.find(l) != -1:
            foundlist += l
    return len(foundlist) == 0

def uses_only(word, list):
    for c in word:
        if list.find(c) == -1:
            return False
    return True

def uses_all(word, list):

    return uses_only(list, word)
    #for c in list:
    #    if word.find(c) == -1:
    #        return False
    #return True

def is_abecedarian(word):
    lower = word.lower()
    lowerLst = list(lower)
    lowerLst.sort()

    if ''.join(lowerLst) == lower:
        return True

    return False

def is_triple_double(word):
    i = 0
    count = 0
    while i < len(word)-1:
        if word[i] == word[i+1]:
            count = count + 1
            if count == 3:
                return True
            i = i + 2
        else:
            count = 0
            i = i + 1
    return False

def is_recurring_palindrome_old(word):
    #strword = str(word)
    #check last for
    if is_palindrome(str(word)[2:]) == False:
        return False
    #add one check last five
    #word += 1
    #strword = str(word)
    if is_palindrome(str(word+1)[1:]) == False:
        return False

    #add one check middle four
    #word += 1
    #strword = str(word)
    if is_palindrome(str(word+2)[1:5]) == False:
        return False
    #add one check all six
    #word += 1
    #strword = str(word)
    return is_palindrome(str(word+3))

def is_recurring_palindrome(word):
    return (is_palindrome(str(word)[2:])
        and is_palindrome(str(word+1)[1:])
        and is_palindrome(str(word+2)[1:5])
        and is_palindrome(str(word+3))
        )

def get_palindrome_ages(mother, daughter, ageDiff):
    returnList = []
    while mother < 120:
        if str(mother)[::-1] == str(daughter).zfill(len(str(mother))):
            returnList.append([str(daughter), str(mother)])
        daughter += 1
        mother = daughter + ageDiff

    return returnList

#print(avoids('superduper', 'az'))

#print(uses_only('cleveland', 'clevandzrt'))

#print(uses_all('zebrahjk', 'zebrahjk'))
#print(is_abecedarian('agNrtz'))
#print(is_triple_double('bookkeeper'))#'mississippi'))
#
# filename = 'words.txt'
# fin = open(filename)
# ln = fin.readline()
# while len(ln) > 0:
#     if is_triple_double(ln.strip()):
#         print(ln.strip())
#     ln = fin.readline()
#
# maxNum = 999999
# curNum = 100000
#
# while curNum <= maxNum:
#     if is_recurring_palindrome(curNum):
#         print(curNum)
#     curNum += 1

ageDiff = 17
daughter = 1
mother = daughter + ageDiff
while ageDiff < 60:
    lst = get_palindrome_ages(mother, daughter, ageDiff)
    if len(lst) > 0:
        print('Age difference is: ' + str(ageDiff))
        print('Daughter - Mother')
        for pair in lst:
            print(pair[0] + ' - ' + pair[1])
    ageDiff += 1
    daughter = 1
    mother = daughter + ageDiff
