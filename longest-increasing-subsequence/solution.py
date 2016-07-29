class Node:
    def __init__(self, val, next_ = None):
        self.val = val
        self.next_ = next_

    def __repr__(self):
        return str(self.val)

def ll_to_list(node):
    list_ = []
    while node:
        list_.insert(0, node)
        node = node.next_
    return list_

def binary_search(list_, element):
    lo = 0
    hi = len(list_)
    while lo < hi:
        mid = lo + (hi - lo) // 2
        # <= for strictly increasing, < for nonstrictly increasing
        if element <= list_[mid]:
            hi = mid
        else: # element <= list_[mid]
            lo = mid + 1
    return lo - 1

def longest_increasing_subsequence(list_):
    heads = []
    for el in list_:
        # get longest list with head < el
        index = binary_search([head.val for head in heads], el)
        # get the next node
        if index == -1: # subsequence length == 1
            next_ = Node(el)
        else: # 0 <= index < len(heads)
            next_ = Node(el, heads[index])

        # if we've found a longer subsequence, append it to our list
        if index == len(heads) - 1:
            heads.append(next_)
        # otherwise update the existing subsequence with the same length
        else:
            heads[index + 1]  = next_
        print [ll_to_list(head) for head in heads]
    return ll_to_list(heads[-1])

list_ = [0, 8, 4, 12, 2, 10, 6, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
print "list:", list_
print longest_increasing_subsequence(list_)
