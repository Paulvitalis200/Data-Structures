class SortMe:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def sort(self, start, end):
        if (end - start + 1) <= 1:
            return self.items

        pivot = self.items[end]
        left = start

        for i in range(left, len(self.items)):
            if self.items[i] < pivot:
                temp = self.items[left]
                self.items[left] = self.items[i]
                self.items[i] = temp
                left += 1

        self.items[end] = self.items[left]
        self.items[left] = pivot

        self.sort(start, left - 1)
        self.sort(left + 1, end)

    def print_me(self):
        return self.items


my_array = SortMe()

my_array.push(58)
my_array.push(899)
my_array.push(8)
my_array.push(200)
my_array.push(30)
my_array.push(100)

print(my_array.print_me())

my_array.sort(0, len(my_array.print_me()) - 1)
print(my_array.print_me())
