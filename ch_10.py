def nested_sum(l):
    total = 0
    for lst in l:
        total += sum(lst)
    return total

def cumsum(l):
    total=0
    retList = []
    for num in l:
        retList.append(num + total)
        total += num
    return retList

def middle(lst):
    return lst[1:-1]

def chop(lst):
    lst.pop()
    del lst[0]

def is_sorted(lst):
    #srt = lst[:].lower()
    # idx = 0
    # while idx < len(lst)-1:
    #     if lst[idx] > lst[idx+1]:
    #         return False
    #     idx += 1
    # return True
    return lst == sorted(lst)

def is_anagram(word1, word2):
    return sorted(word1) == sorted(word2)

def has_duplicates(lst):
    srt = sorted(lst)

    for idx in range(len(srt)-1):
        if srt[idx] == srt[idx+1]:
            return True
    return False

# t = [[1, 2], [3], [4, 5, 6]]
# print(nested_sum(t))

t=[1,2,3,4,5,6,7]
# print(cumsum([1,2,3]))
#
# print(middle(t))
#
# print(t)
# print(chop(t))
# print(t)

#t = ['a', 'b', 'z', 'c', 'd']
# print(is_sorted(t))
# print(is_anagram('cinema', 'iceman'))

print(has_duplicates(t))
