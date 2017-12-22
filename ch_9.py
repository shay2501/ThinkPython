

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

#words_without_e('words.txt')

#print(avoids('superduper', 'az'))

print(uses_only('cleveland', 'clevandzrt'))
