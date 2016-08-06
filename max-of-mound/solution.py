def get_max(mound):
    lo = 0
    hi = len(mound) - 1
    while lo < hi:
        mid = (lo + hi)  // 2
        if mound[mid] < mound[mid + 1]:
            lo = mid + 1
        else:
            hi = mid
    return mound[lo]

mound = [1]
mound = [1,2]
mound = [2,1]
mound = [1,3,4,9,7,5,2]
mound = [1,3,4,9,10,7,5,2]
print mound
print get_max(mound)
