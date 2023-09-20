class Heap:
    def __init__(self):
        self.heap = [0]

    def push(self, val):
        self.heap.append(val)
        i = len(self.heap) - 1

        # percolate up
        while self.heap[i] < self.heap[i//2]:
            temp = self.heap[i]
            self.heap[i] = self.heap[i//2]
            self.heap[i//2] = temp
            i = i // 2

# Time commplexity: Height  of tree. We know that tree will alwasys  be balanced: O (log n)

    def pop(self):
        # If we only havve dummy element
        if len(self.heap) == 1:
            return None
        
        # When we have one element in our heap
        if len(self.heap == 2):
            return self.heap.pop()
        
        # Initialize our result to the first element in our heap
        res = self.heap[1]

        # Move last value to root. We remove it
        self.heap[1] =  self.heap.pop()
        i = 1

        # Percolate down
        # While we at least have a left child
        while 2 * i < len(self.heap):
            if (2 * i + 1 < len(self.heap) and 
                self.heap[2 * i + 1] < self.heap[2*i] and
                self.heap[i] > self.heap[2 *  i + 1]):
                # Swap right child
                temp = self.heap[i]
                self.heap[i] = self.heap[2 * i + 1]
                self.heap[2 * i + 1] = temp
                i = 2 * i + 1
            elif self.heap[i] > self.heap[2 * i]:
                # Swap left child
                tmp = self.heap[i]
                self.heap[i] = self.heap[2  *  i]
                self.heap[2* i] = tmp
                i = 2 * i
            else:
                break
        return res

    # Time complexity: O(log n) 

    def heapify(self, arr):
        # 0-th position is moved to the end
        arr.append(arr[0])

        self.heap = arr
        cur = (len(self.heap) - 1) // 2
        while cur > 0:
            # Percolate down
            i = cur
            while 2 * i < len(self.heap):
                if (2 * i + 1 < len(self.heap) and 
                self.heap[2 * i + 1] < self.heap[2 * i] and 
                self.heap[i] > self.heap[2 * i + 1]):
                    # Swap right child
                    tmp = self.heap[i]
                    self.heap[i] = self.heap[2 * i + 1]
                    self.heap[2 * i + 1] = tmp
                    i = 2 * i + 1
                elif self.heap[i] > self.heap[2 * i]:
                    # Swap left child
                    tmp = self.heap[i]
                    self.heap[i] = self.heap[2 * i]
                    self.heap[2 * i] = tmp
                    i = 2 * i
                else:
                    break
            cur -= 1
