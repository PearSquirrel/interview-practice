def longest_alternating_subsequence(list_):
    up = list_[0] < list_[1]
    las = [list_[0]]
    for i in xrange(2, len(list_)):
        if (up and list_[i-1] > list_[i]) or (not up and list_[i-1] < list_[i]):
            las.append(list_[i-1])
            up = not up
    las.append(list_[-1])
    return las

list_ = [3,2,4,6,7,1,0,8,9]
list_ = [1,2,3,3,3,1,3,7,2,3,3,3,1,4,5,5,5,1,2]
list_ = [3,1,3,3,4,2,1,7]
print "list:", list_
print longest_alternating_subsequence(list_)
