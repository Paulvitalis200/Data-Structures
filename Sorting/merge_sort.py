def merge_sort(nums, left, right):
    if left == right:
        return nums

    mid = (left + right) // 2

    merge_sort(nums, left, mid)

    merge_sort(nums, mid + 1, right)

    merge(nums, left, mid, right)

    return nums


def merge(nums, left, mid, right):
    LEFT = nums[left:mid+1]
    RIGHT = nums[mid+1:right+1]

    i, j, k = left, 0, 0

    while j < len(LEFT) and k < len(RIGHT):
        if LEFT[j] <= RIGHT[k]:
            nums[i] = LEFT[j]
            j += 1
        else:
            nums[i] = RIGHT[k]
            k += 1

        i += 1

    while j < len(LEFT):
        nums[i] = LEFT[j]
        i += 1
        j += 1

    while k < len(RIGHT):
        nums[i] = RIGHT[k]
        i += 1
        k += 1


my_nums = [7888, 19, 39, 1999, 388, 21, 2]

print(merge_sort(my_nums, 0, len(my_nums) - 1))


class SortMe:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def print_array(self):
        return self.items

    def merge_sort(self, arr, s, e):
        if (e - s + 1) == 1:
            return arr

        mid = (s + e) // 2

        self.merge_sort(arr, s, mid)
        self.merge_sort(arr, mid + 1, e)

        self.merge(arr, s, mid, e)

    def merge(self, arr, s, m, e):
        L = arr[s:m+1]
        R = arr[m+1:e+1]

        l, j, k = s, 0, 0

        while j < len(L) and k < len(R):
            if L[j] <= R[k]:
                arr[l] = L[j]
                j += 1
            else:
                arr[l] = R[k]
                k += 1
            l += 1

        while j < len(L):
            arr[l] = L[j]
            j += 1
            l += 1

        while k < len(R):
            arr[l] = R[k]
            k += 1
            l += 1

    def length(self):
        return len(self.items)


my_array = SortMe()
my_array.push(577)
my_array.push(54)
my_array.push(1000)
my_array.push(3)
my_array.push(57)
my_array.push(351)
my_array.push(788)
my_array.push(351)
my_array.push(788)
print(my_array.print_array())
print(my_array.length())
my_array.merge_sort(my_array.print_array(), 0, my_array.length())
print(my_array.print_array())
