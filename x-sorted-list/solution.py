from heapq import heappush, heappop

def sort(x, x_sorted):
    # if you can store the whole list in memory, just sort it regularly
    if len(x_sorted) <= x:
        x_sorted.sort()

    # add the first x items to a min-heap
    heap = []
    for item in x_sorted[:x]:
        heappush(heap, item)

    # repeatedly take the min of x items to sort the list
    i = 0
    while i < len(x_sorted):
        x_sorted[i] = heappop(heap)
        if i + x < len(x_sorted):
            heappush(heap, x_sorted[i+x])
        i += 1

list_ = [4,3,2,1,8,7,6,5]
print "original:", list_
sort(4, list_)
print "sorted:", list_
