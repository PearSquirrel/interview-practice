def merge_sort(a):
    b = [0] * len(a)
    left = 0
    right = len(a)
    internal_merge_sort(a, b, left, right)
    return b

def internal_merge_sort(a, b, left, right):
    # base case (nothing to do)
    mid = (left + right) // 2
    if left >= mid:
        return

    # recursively sort the two halves
    internal_merge_sort(a, b, left, mid)
    internal_merge_sort(a, b, mid, right)

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

input_ = [1,5,4,3,2,4,6, 40, 30, 20, 34, 66, 5, 1, -1]
print input_
print merge_sort(input_)
