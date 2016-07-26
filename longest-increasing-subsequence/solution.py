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

def longest_increasing_subsequence(list_):
    heads = []
    # TODO: replace linear search with a binary search
    """
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
    """

    for i, el in enumerate(list_):
        # get longest list with head < list_[i]
        index = 0
        while index < len(heads) and el >= heads[index].val:
            index += 1
        if index >= len(heads):
            heads.append([])
        if index == 0:
            heads[index] = Node(el)
        else:
            heads[index] = Node(el, heads[index-1])

    return ll_to_list(heads[len(heads)-1])

list_ = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
print "list:", list_
print longest_increasing_subsequence(list_)
