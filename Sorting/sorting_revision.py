class Sorting:
    def __init__(self, nums):
        self.nums = nums

    def insertion_sort(self):
        for i in range(1, len(self.nums)):
            j = i - 1
            while self.nums[j] > self.nums[j+1] and j >= 0:
                temp = self.nums[j+1]
                self.nums[j+1] = self.nums[j]
                self.nums[j] = temp
                j -= 1
            
    
    def merge_sort(self, start, end):
        if start == end:
            return self.nums
        
        mid = (start + end) // 2

        self.merge_sort(start, mid)
        self.merge_sort(mid+1, end)

        self.merge(self.nums, start, mid, end)

    def merge(self, nums, start, mid, end):
        LEFT = nums[start:mid+1]
        RIGHT = nums[mid+1:end+1]

        i, j, k = start, 0, 0

        while j < len(LEFT) and k < len(RIGHT):
            if LEFT[j] < RIGHT[k]:
                self.nums[i] = LEFT[j]
                j += 1
            else:
                self.nums[i] = RIGHT[k]
                k += 1

            i += 1

        while j < len(LEFT):
            self.nums[i] = LEFT[j]
            j += 1
            i += 1

        while k < len(RIGHT):
            self.nums[i] = RIGHT[k]
            k += 1
            i += 1

    def quick_sort(self, start, end):
        if end - start + 1 <= 1:
            return self.nums
        
        pivot, left = self.nums[end], start

        for i in range(start, end):
            if self.nums[i] < pivot:
                temp = self.nums[left]
                self.nums[left] = self.nums[i]
                self.nums[i] = temp
                left += 1

        self.nums[end] = self.nums[left]
        self.nums[left] = pivot 

        self.quick_sort(start, left - 1)
        self.quick_sort(left + 1, end)

    def kth_largest(self, k):
        k = len(self.nums) - k

        def quick_sort(start, end):

            pivot = self.nums[end]
            left = start

            for i in range(start, end):
                if self.nums[i] <= pivot:
                    temp = self.nums[left]
                    self.nums[left] = self.nums[i]
                    self.nums[i] = temp
                    left += 1

            self.nums[end] = self.nums[left]
            self.nums[left] = pivot

            if left > k:
                return quick_sort(start, left - 1)
            elif left < k:
                return quick_sort(left + 1, end)
            else:
                return self.nums[left]
            
        return quick_sort(0, len(self.nums) - 1)

        

    def sort_colors(self, colors):

        counts = [0,0,0]

        for i in range(len(colors)):
            counts[colors[i]] += 1

        n = 0

        for i in range(len(counts)):
            for j in range(counts[i]):
                colors[n] = i
                n += 1

        return colors
    
    def get_numbers(self):
        return self.nums

start_numbers = [19,2,20,45,23,10,1,5, 7, 9]

numbers = Sorting(start_numbers)
# numbers.insertion_sort()
# numbers.merge_sort(0, len(start_numbers) - 1)
# numbers.quick_sort(0, len(start_numbers) - 1)
# print(numbers.get_numbers())
print(numbers.findKthLargest(start_numbers, 4))
print(numbers.kth_largest(4))
print(numbers.sort_colors([1,1,0,0,2,2,1]))