def quick_sort(nums, start, end):
    if end - start + 1 <= 1:
        return

    pivot = nums[end]
    L = start

    for i in range(start, end):
        if nums[i] < pivot:
            temp = nums[L]
            nums[L] = nums[i]
            nums[i] = temp
            L += 1

    nums[end] = nums[L]
    nums[L] = pivot

    quick_sort(nums, start, L - 1)
    quick_sort(nums, L + 1, end)

    return nums

def quicksort(nums, start, end):
    if end - start + 1  <= 1:
        return
    
    pivot = nums[end]
    L = start

    for i  in range(start, len(nums)):
        if  nums[i] < pivot:
            temp = nums[L]
            nums[L] = nums[i]
            nums[i] =  temp
            L += 1

    nums[end] = nums[L]
    nums[L] = pivot

    quicksort(nums, start, L - 1)
    quicksort(nums, L + 1, end)

    return nums



class QuickSort:
    def __init__(self):
        self.items = []

    def print_array(self):
        return self.items

    def push(self, item):
        self.items.append(item)

    def sort(self, arr, start, end):
        if (end - start + 1 <= 1):
            return arr

        pivot = arr[end]
        left = start

        for i in range(left, len(arr)):
            if (arr[i] < pivot):
                temp = arr[left]
                arr[left] = arr[i]
                arr[i] = temp
                left += 1

        arr[end] = arr[left]
        arr[left] = pivot

        quick_sort(arr, start, left - 1)
        quick_sort(arr, left + 1, end)

    def len(self):
        return len(self.items)


sorting = QuickSort()
sorting.push(44)
sorting.push(3)
sorting.push(122)
sorting.push(7)
sorting.push(400)
sorting.push(33)
sorting.push(34)
sorting.push(333)

# print(sorting.print_array())

sorting.sort(sorting.print_array(), 0, sorting.len() - 1)

print(sorting.print_array())
nums = [29,394,1,34,2,55,3]

print(quicksort(nums, 0, len(nums) - 1))