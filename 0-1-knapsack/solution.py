#   | 0 1 4 6 2
# --+----------
# 0 | 0 0 0 0 0
# 1 | 0 1 1 1 1
# 2 | 0 1 1 1 2
# 3 | 0 1 1 1 3
# 4 | 0 1 4 4 4
# 5 | 0 1 5 5 5
# 6 | 0 1 5 6 6

def transpose(matrix):
    return [list(i) for i in zip(*matrix)]

def print_grid(grid):
    for i, list_ in enumerate(transpose(grid)):
        print i, list_
    print ""

def knapsack(values, weights, capacity):
    m = [[0 for j in range(capacity+1)] for i in range(len(values)+1)]
    for i in xrange(0, len(values)):
        for j in xrange(0, capacity + 1): # j == remaining capacity
            # if the item can't fit, use best bag without the item
            if weights[i] > j:
                m[i+1][j] = m[i][j]
            # else use max(best bag without the item, best bag with the item)
            else:
                m[i+1][j] = max(m[i][j], m[i][j-weights[i]] + values[i])
    print_grid(m)
    return m[-1][-1]

capacity = 6
values   = [1,4,6,2]
weights  = [1,4,6,2]
print "capacity:", capacity
print "values:", values
print "weights:", weights
result =  knapsack(values, weights, capacity)
print "knapsack result:", result
