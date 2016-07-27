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

def add_to_list(heads, index, el):
    if index >= len(heads):
        heads.append([])
    if index == 0:
        heads[index] = Node(el)
    else:
        heads[index] = Node(el, heads[index-1])

def longest_alternating_subsequence(list_):
    heads = []

    # iterate through the input array
    for i, el in enumerate(list_):
        # add to troughs
        # find the largest list with el > its head
        index = len(heads) - 1
        found = False

        # break if you found the largest list or ran out of lists
        while index >= 0 and not found:
            # index % 2 == 0 <==> index corresponds to a trough
            if index % 2 == 0 and el > heads[index].val:
                add_to_list(heads, index + 1, el)
                found = True
            index -= 1
        # smaller than anything else-- replace the head of the smallest list
        if not found:
            add_to_list(heads, 0, el)

        # add to peaks
        index = len(heads) - 1
        found = False
        while index >= 0 and not found:
            # index % 2 == 1 <==> index corresponds to a peak
            if index % 2 == 1 and el < heads[index].val:
                add_to_list(heads, index + 1, el)
                found = True
            index -= 1

        # larger than anything else-- replace the head of the largest existing list
        if not found:
            add_to_list(heads, len(heads)-1, el)

        # print out all the lists
        #print "lists:"
        #for head in heads:
            #print ll_to_list(head)

    return ll_to_list(heads[len(heads)-1])

list_ = [3,2,4,6,7,1,0,8,9]
print "list:", list_
print longest_alternating_subsequence(list_)
