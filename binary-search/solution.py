def binary_search(list_, element):
    lo = 0
    hi = len(list_)
    while hi > lo:
        mid = lo + (hi - lo) // 2
        if list_[mid] == element:
            return mid
        if list_[mid] < element:
            lo = mid + 1
        else: # list_[mid] > element
            hi = mid
    return -1

def str_index(list_, index):
    list2 = list(list_)
    list2[index] = '^'
    return str(list2).index('^')

list_ = [1,2,3,4,4,4,4,5,6,7,7,7,8,9,10,11,12]
element = 5
print list_
print "looking for", element, "..."
index = binary_search(list_, 5)
if index < 0:
    print element, "not found."
else:
    print list_
    print ' ' * (str_index(list_, index) - 1) + '^'
