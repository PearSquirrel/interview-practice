def inversion_count(a):
    b = [0] * len(a)
    left = 0
    right = len(a)
    return internal_merge_sort(a, b, left, right)

def internal_merge_sort(a, b, left, right):
    # base case (nothing to do)
    mid = (left + right) // 2
    if left >= mid:
        return 0

    inversions = 0

    # recursively sort the two halves
    inversions += internal_merge_sort(a, b, left, mid)
    inversions += internal_merge_sort(a, b, mid, right)

    # merge two sorted lists (the two halves)
    sorted_index = left
    left_index = left
    right_index = mid

    # while neither list is empty
    while left_index < mid and right_index < right:
        # if the left list has the next element
        if a[left_index] <= a[right_index]:
            # store the left list's element in a secondary array
            b[sorted_index] = a[left_index]
            left_index += 1
        else:
            # store the right lists' element in a secondary array
            b[sorted_index] = a[right_index]
            inversions += mid - left_index
            right_index += 1
        sorted_index += 1

    # if the right list is empty, just copy the left list over
    while left_index < mid:
        b[sorted_index] = a[left_index]
        left_index += 1
        sorted_index += 1

    # if the left list is empty, just copy the right list over
    while right_index < right:
        b[sorted_index] = a[right_index]
        right_index += 1
        sorted_index += 1

    # copy the updated secondary array section back to the original
    copy_index = left
    while copy_index < right:
        a[copy_index] = b[copy_index]
        copy_index += 1

    return inversions

input_ = [5,4,3,2,1]
print input_
print "inversions:", inversion_count(input_)
