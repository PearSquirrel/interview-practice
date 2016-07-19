from heapq import heappush, heappop

class Node:
    def __init__(self, value, list_index, index):
        self.value = value
        self.list_index = list_index
        self.index = index

    def __cmp__(self, other):
        return self.value - other.value

    def __repr__(self):
        return "(%s, %s, %s)" % (self.value, self.list_index, self.index)

def min_range(lists):
    # convert each list element from int to Node
    for list_index, list_ in enumerate(lists):
        for index, value in enumerate(list_):
            lists[list_index][index] = Node(value, list_index, index)

    # initialize tracked values
    min_range = 100000000
    max_ = Node(-1, 0, 0)

    # populate a min-heap with the lists' left-most elements and track the max
    h = []
    for list_ in lists:
        heappush(h, list_[0])
        if list_[0].value > max_.value:
            max_ = list_[0]

    # track the current minimum range, stopping once a list has been depleted
    while True:
        # grab the minimum from the heap
        min_ = heappop(h)
        range_ = max_.value - min_.value

        # update the min_range if needed
        if range_ < min_range:
            min_range = range_
            min_l = min_.value
            min_r = max_.value

        # if a list has been processed, the smallest range has been found
        if min_.index >= len(lists[min_.list_index]) - 1:
            return (min_l, min_r)

        # if there exists a neighbor, add it to the heap
        neighbor = lists[min_.list_index][min_.index + 1]
        heappush(h, neighbor)
        if neighbor.value > max_.value:
            max_ = neighbor

# main program
input_ = [[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]]
print "input:", input_
print "minimum range:", min_range(input_)
