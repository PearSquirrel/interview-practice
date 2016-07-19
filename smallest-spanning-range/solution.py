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
    for list_index, _list in enumerate(lists):
        for index, value in enumerate(_list):
            lists[list_index][index] = Node(value, list_index, index)

    # initialize tracked values
    min_range = 100000000
    _max = Node(-1, 0, 0)

    # populate a min-heap with the lists' left-most elements and track the max
    h = []
    for _list in lists:
        heappush(h, _list[0])
        if _list[0].value > _max.value:
            _max = _list[0]

    # track the current minimum range, stopping once a list has been depleted
    while True:
        # grab the minimum from the heap
        _min = heappop(h)
        _range = _max.value - _min.value

        # update the min_range if needed
        if _range < min_range:
            min_range = _range
            min_l = _min.value
            min_r = _max.value

        # if a list has been processed, the smallest range has been found
        if _min.index >= len(lists[_min.list_index]) - 1:
            return (min_l, min_r)

        # if there exists a neighbor, add it to the heap
        neighbor = lists[_min.list_index][_min.index + 1]
        heappush(h, neighbor)
        if neighbor.value > _max.value:
            _max = neighbor

# main program
_input = [[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]]
print "input:", _input
print "minimum range:", min_range(_input)
