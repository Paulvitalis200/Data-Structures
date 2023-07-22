# def sort(nums):
#     indexing_length = len(nums) - 1

#     for i in range(indexing_length):
#         min_pos = i
#         for j in range(i, indexing_length + 1):
#             if nums[j] < nums[min_pos]:
#                 min_pos = j

#         temp = nums[i]
#         nums[i] = nums[min_pos]
#         nums[min_pos] = temp

#     return nums


def sort(nums):
    indexing_length = len(nums) - 1

    for i in range(indexing_length):
        min_pos = i

        for j in range(i, indexing_length+1):
            if nums[j] < nums[min_pos]:
                min_pos = j

        temp = nums[i]
        nums[i] = nums[min_pos]
        nums[min_pos] = temp

    return nums


print(sort([48, 30, 4, 29, 199, 39, 43, 91, 19]))
