def knapsack(values, weights, capacity):
    m = [[0] * capacity] * len(values)
    for i in xrange(1, len(values)):
        for j in xrange(0, capacity):
            if weights[i-1] > j:
                m[i][j] = m[i-1][j]
            else:
                m[i][j] = max(m[i-1][j], m[i-1][j-weights[i-1]] + values[i-1])
    return m[-1][-1]

values   = [1,2,3]
weights  = [3,2,3]
capacity = 6
print "values:", values
print "weights:", weights
print "capacity:", capacity
print knapsack(values, weights, capacity)
