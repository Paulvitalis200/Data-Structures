# def merge_sort(arr, left, right):
#     if left == right:
#         return arr

#     mid = (left + right) // 2

#     merge_sort(arr, left, mid)
#     merge_sort(arr, mid+1, right)

#     merge(arr, left, mid, right)

#     return arr


# def merge(arr, l, m, r):
#     left = arr[l: m+1]
#     right = arr[m+1:r+1]

#     i, j, k = l, 0, 0

#     while j < len(left) and k < len(right):
#         if left[j] <= right[k]:
#             arr[i] = left[j]
#             j += 1
#         else:
#             arr[i] = right[k]
#             k += 1

#         i += 1

#     while j < len(left):
#         arr[i] = left[j]
#         j += 1
#         i += 1

#     while k < len(right):
#         arr[i] = right[k]
#         k += 1
#         i += 1


# nums = [84, 44, 22, 100, 293, 223]

# print(merge_sort(nums, 0, len(nums)-1))


def merge_sort(nums, left, right):
    if left == right:
        return nums

    mid = (left + right) // 2
    merge_sort(nums, left, mid)
    merge_sort(nums, mid+1, right)

    merge(nums, left, mid, right)

    return nums


def merge(nums, l, m, r):
    left = nums[l:m+1]
    right = nums[m+1:r+1]

    i, j, k = l, 0, 0

    while j < len(left) and k < len(right):
        if left[j] <= right[k]:
            nums[i] = left[j]
            j += 1
        else:
            nums[i] = right[k]
            k += 1
        i += 1

    while j < len(left):
        nums[i] = left[j]
        i += 1
        j += 1

    while k < len(right):
        nums[i] = right[k]
        i += 1
        k += 1


my_nums = [7888, 19, 39, 1999, 388, 21, 2]

print(merge_sort(my_nums, 0, len(my_nums) - 1))
