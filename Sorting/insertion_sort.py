
# def insertion_sort(nums):
#     for i in range(1, len(nums)):
#         j = i - 1

#         while j >= 0 and nums[j+1] < nums[j]:
#             temp = nums[j+1]
#             nums[j+1] = nums[j]
#             nums[j] = temp
#             j -= 1
#     return nums


# my_nums = [10, 9, 8, 7, 6, 5, 4]

# print(insertion_sort(my_nums))

# Time complexity: Worst case - O(n)2


num_list = [38, 39, 1, 32, 44, 91]


def insertion_sort(nums):

    for i in range(1, len(nums)):
        j = i - 1

        while j >= 0 and nums[j+1] < nums[j]:
            temp = nums[j + 1]
            nums[j+1] = nums[j]
            nums[j] = temp
            j -= 1

    return nums


print(insertion_sort(num_list))
