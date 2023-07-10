
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

# Time complexity: Worst case - O(n)2 Best O(n)


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


# print(insertion_sort(num_list))


class SortMe:
    def __init__(self):
        self.items = []

    def sort_array(self):
        for i in range(1, len(self.items)):
            j = i - 1
            while (j >= 0 and self.items[j] > self.items[j+1]):
                temp = self.items[j+1]
                self.items[j+1] = self.items[j]
                self.items[j] = temp
                j -= 1

    def push(self, item):
        self.items.append(item)

    def print_array(self):
        print(self.items)


items = SortMe()

items.push(45)
items.push(33)
items.push(100)
items.push(4)

items.print_array()

items.sort_array()

items.print_array()
