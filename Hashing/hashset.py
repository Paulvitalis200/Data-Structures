class ListNode:
    def __init__(self, key):
        self.key = key
        self.next = None

class MyHashSet:

    def __init__(self):
        # Initialize hashset with index from 0 to 9999
        # We use a linked list for chaining
        self.hashset = [ListNode(0) for i in range(10**4)]
        

    def add(self, key: int) -> None:
        # get index key will map to
        index = key % len(self.hashset)
        # get head/current pointer of linkedd list
        cur = self.hashset[index]
        while cur.next:
            # In case we detect a duplicate value
            # We do cur.next to skip thedummy node
            if cur.next.key == key:
                return
            cur = cur.next
        
        cur.next = ListNode(key)
        
    def remove(self, key: int) -> None:
        # get index key will map to
        index = key % len(self.hashset)
        # get head/current pointer of linkedd list
        cur = self.hashset[index]
        while cur.next:
            # In case the value exists, we remove it
            # We do cur.next to skip thedummy node
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur = cur.next

        

    def contains(self, key: int) -> bool:
         # get index key will map to
        index = key % len(self.hashset)
        # get head/current pointer of linkedd list
        cur = self.hashset[index]
        while cur.next:
            # In case the value exists, we return true
            # We do cur.next to skip thedummy node
            if cur.next.key == key:
                return True
            cur = cur.next
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)