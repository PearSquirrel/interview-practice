def max_surpasser(input_):
    original_indices = range(len(input_))
    tmp = [0] * len(input_)
    surpassers = [0] * len(input_)
    left = 0
    right = len(input_)
    internal_merge_sort(input_, original_indices, tmp, surpassers, left, right)
    print "input     :", input_
    print "sorted    :", [input_[x] for x in original_indices]
    print "surpassers:", surpassers
    print "maximum surpasser:",  max(surpassers)

def internal_merge_sort(a, o, t, s, left, right):
    # base case (nothing to do)
    mid = (left + right) // 2
    if left >= mid:
        return

    # recursively sort the two halves
    internal_merge_sort(a, o, t, s, left, mid)
    internal_merge_sort(a, o, t, s, mid, right)

    # merge two sorted lists (the two halves)
    sorted_index = left
    left_index = left
    right_index = mid

    # while neither list is empty
    while left_index < mid and right_index < right:
        # if the left list has the next element
        if a[o[left_index]] < a[o[right_index]]:
            # store the left list's element in a secondary array
            t[sorted_index] = o[left_index]
            s[o[left_index]] += right - right_index
            left_index += 1
        else:
            # store the right lists' element in a secondary array
            t[sorted_index] = o[right_index]
            right_index += 1
        sorted_index += 1

    # if the right list is empty, just copy the left list over
    while left_index < mid:
        t[sorted_index] = o[left_index]
        left_index += 1
        sorted_index += 1

    # if the left list is empty, just copy the right list over
    while right_index < right:
        t[sorted_index] = o[right_index]
        right_index += 1
        sorted_index += 1

    # copy the updated secondary array section back to the original
    copy_index = left
    while copy_index < right:
        o[copy_index] = t[copy_index]
        copy_index += 1

input_ = [2,7,5,5,2,7,0,8,1]
max_surpasser(input_)
