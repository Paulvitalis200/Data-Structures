class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        cur = self.head
        while cur.next:
            cur = cur.next

        cur.next = new_node

    def insert_at_pos(self, data, pos):
        new_node = Node(data)

        cur = self.head

        if self.head is None:
            self.head = new_node
            return

        if pos == 0:
            self.head = new_node
            new_node.next = cur
            return

        prev = None
        count = 0
        while count != pos and cur:
            prev = cur
            cur = cur.next
            count += 1

        if not cur:
            return

        nxt = prev.next
        prev.next = new_node
        new_node.next = nxt

    def delete_at_pos(self, pos):
        count = 0
        cur = self.head
        if not self.head:
            return

        if pos == 0:
            self.head = cur.next
            return

        prev = None
        while count != pos and cur:
            count += 1
            prev = cur
            cur = cur.next

        if cur is None:
            return

        prev.next = cur.next
        cur = None

    def delete_node(self, data):
        cur_node = self.head

        if cur_node and cur_node.data == data:
            self.head = cur_node.next
            cur_node = None
            return

        prev = None
        while cur_node and cur_node.data != data:
            prev = cur_node
            cur_node = cur_node.next

        if cur_node is None:
            return

        prev.next = cur_node.next
        cur_node = None

    def length(self):
        cur = self.head

        count = 0
        while cur:
            count += 1
            cur = cur.next

        return count

    def len_recursive(self, node):
        if node is None:
            return 0
        return 1 + self.len_recursive(node.next)

    def swap_nodes(self, key_1, key_2):
        if key_1 == key_2:
            return

        prev_1 = None
        cur_1 = self.head
        while cur_1 and cur_1.data != key_1:
            prev_1 = cur_1
            cur_1 = cur_1.next

        prev_2 = None
        cur_2 = self.head
        while cur_2 and cur_2.data != key_2:
            prev_2 = cur_2
            cur_2 = cur_2.next

        if not cur_1 or not cur_2:
            return None

        if prev_1:
            prev_1.next = cur_2
        else:
            self.head = cur_2

        if prev_2:
            prev_2.next = cur_1
        else:
            self.head = cur_1

        cur_1.next, cur_2.next = cur_2.next, cur_1.next

        if key_1 == key_2:
            return

        prev_1 = None
        cur_1 = self.head
        while cur_1 and cur_1.data != key_1:
            prev_1 = cur_1
            cur_1 = cur_1.next

        prev_2 = None
        cur_2 = self.head
        while cur_2 and cur_2.data != key_2:
            prev_2 = cur_2
            cur_2 = cur_2.next

        if not cur_1 or not cur_2:
            return None

        if prev_1:
            prev_1.next = cur_2
        else:
            self.head = cur_2

        if prev_2:
            prev_2.next = cur_1
        else:
            self.head = cur_1

        cur_1.next, cur_2.next = cur_2.next, cur_1.next

    # A -> B -> C -> D -> 0
    # D -> C -> B -> A -> 0
    # A <- B <- C <- D <- 0
    def reverse_iterative(self):
        prev = None
        cur = self.head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur.next = nxt
        self.head = prev

    def merge_sorted(self, llist):
        p = self.head
        q = llist.head
        s = None

        if not p:
            return q
        if not q:
            return p

        if p and q:
            if p.data <= q.data:
                s = p
                p = s.next
            else:
                s = q
                q = s.next

            new_head = s

        while p and q:
            if p.data <= q.data:
                s.next = p
                s = p
                p = s.next
            else:
                s.next = q
                s = q
                q = s.next

        if not p:
            s.next = q
        if not q:
            s.next = p

        return new_head

    def remove_duplicates(self):

        cur = self.head

        prev = None

        dup_values = dict()

        while cur:
            if cur.data in dup_values:
                # Remove node:
                prev.next = cur.next
                cur = None
            else:
                # Have not encountered element before
                dup_values[cur.data] = 1
                prev = cur
            cur = prev.next

    def remove_dups_two(self):
        cur = self.head
        prev = None
        dup_values = dict()

        while cur:
            if cur.data not in dup_values:
                dup_values[cur.data] = 1
                prev = cur
            else:
                prev.next = cur.next
                cur = None
            cur = prev.next

    def nth_to_last(self, n):
        cur_node = self.head

        total_length = self.length()

        while cur_node and n != total_length:
            cur_node = cur_node.next
            total_length -= 1

        if cur_node is None:
            return
        return cur_node.data

    def count_occurrences(self, data):
        cur = self.head

        # hash_map = dict()
        # while cur:
        #     if cur.data in hash_map:
        #         hash_map[cur.data] += 1
        #     else:
        #         hash_map[cur.data] = 1
        #     cur = cur.next

        # if data not in hash_map:
        #     return 'Data does not exist'
        # return hash_map[data]
        count = 0
        while cur:
            if cur.data == data:
                count += 1
            cur = cur.next

        return count

    def count_occurrences_recursive(self, node, data):
        if node is None:
            return 0

        if node.data == data:
            return 1 + self.count_occurrences_recursive(node.next, data)
        else:
            return self.count_occurrences_recursive(node.next, data)

    def rotate(self, k):
        # p = self.head
        # q = self.head

        # count = 0
        # prev = None

        # while p and count != k:
        #     prev = p
        #     p = p.next
        #     q = q.next
        #     count += 1
        # p = prev

        # while q:
        #     prev = q
        #     q = q.next

        # q = prev

        # q.next = self.head
        # self.head = p.next
        # p.next = None

        p = self.head
        q = self.head

        count = 0
        prev = None
        while p and count != k:
            prev = p
            p = p.next
            count += 1
        p = prev

        while q:
            prev = q
            q = q.next
        q = prev

        q.next = self.head
        self.head = p.next
        p.next = None


# Original list:
# 1 -> 6  -> 1 -> 4 -> 2 -> 2

#  Remove duplicates
# 1  -> 6 -> 4 -> 2


# llist = LinkedList()
# llist.append(1)
# llist.append("B")
# llist.append("C")
# llist.append("D")
# # llist.delete_at_pos(0)
# # llist.delete_node("B")
# llist.insert_at_pos("F", 0)
# llist.print_list()
# print(llist.length())
# print(llist.len_recursive(llist.head))
# llist.swap_nodes("C", "D")
# llist.print_list()
# llist_1 = LinkedList()
# llist_2 = LinkedList()

# llist_1.append(1)
# llist_1.append(5)
# llist_1.append(7)
# llist_1.append(9)
# llist_1.append(10)

# llist_2.append(2)
# llist_2.append(3)
# llist_2.append(4)
# llist_2.append(6)
# llist_2.append(8)

# llist_1.merge_sorted_two(llist_2)
# llist_1.print_list()

    def merge_sorted_new(self, new_list):
        p = self.head
        q = new_list.head
        s = None

        if not p:
            return q
        if not q:
            return p

        if p and q:
            if p.data <= q.data:
                s = p
                p = s.next
            else:
                s = q
                q = s.next
            new_head = s

        while p and q:
            if p.data <= q.data:
                s.next = p
                s = p
                p = s.next
            else:
                s.next = q
                s = q
                q = s.next

        if not p:
            s.next = q
        if not q:
            s.next = p

        return new_head

    def reverse_latest(self):
        cur = self.head

        prev = None

        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        self.head = prev

    def remove_dups_twsso(self):
        cur = self.head

        hash_map = dict()
        prev = None
        while cur:
            if cur.data in hash_map:
                prev.next = cur.next
                cur = None
                cur = prev.next
            else:
                hash_map[cur.data] = 1
                prev = cur
                cur = prev.next

    def is_palindrome(self):
        # Method 1:
        # s = ""
        # p = self.head
        # while p:
        #     s += p.data
        #     p = p.next

        # return s == s[::-1]

        # Method 2
        # p = self.head
        # s = []
        # while p:
        #     s.append(p.data)
        #     p = p.next

        # p = self.head
        # while p:
        #     data = s.pop()
        #     if p.data != data:
        #         return False
        #     p = p.next

        # return True

        # Method 3
        # s = ""
        # cur = self.head
        # while cur:
        #     s += cur.data
        #     cur = cur.next

        # return s == s[::-1]
        s = []
        cur = self.head
        while cur:
            s.append(cur.data)
            cur = cur.next

        cur = self.head
        while cur:
            data = s.pop()
            if data != cur.data:
                return False
            cur = cur.next

        return True

        # Example palindromes:
        # RACECAR, RADAR

        # Example non-palindromes:
        # TEST, ABC, HELLO

    def move_tail_to_head(self):
        last = self.head
        second_to_last = None

        while last.next:
            second_to_last = last
            last = last.next

        last.next = self.head
        second_to_last.next = None
        self.head = last

    def sum_two_lists(self, llist):
        p = self.head
        q = llist.head

        sum_list = LinkedList()

        carry = 0
        while p or q:
            if not p:
                i = 0
            else:
                i = p.data
            if not q:
                j = 0
            else:
                j = q.data

            s = i + j + carry

            if s >= 10:
                carry = 1
                remainder = s % 10
                sum_list.append(remainder)
            else:
                carry = 0
                sum_list.append(s)
            if p:
                p = p.next
            if q:
                q = q.next
        sum_list.print_list()

    def sum_two_revision(self, llist):
        p = self.head
        q = llist.head

        carry = 0

        sum_list = LinkedList()

        while p or q:
            if not p:
                i = 0
            else:
                i = p.data
            if not q:
                j = 0
            else:
                j = q.data

            s = i + j + carry

            if s >= 10:
                carry = 1
                remainder = s % 10
                sum_list.append(remainder)
            else:
                carry = 0
                sum_list.append(s)

            if p:
                p = p.next
            if q:
                q = q.next

        sum_list.print_list()


llist = LinkedList()
llist_2 = LinkedList()
llist_3 = LinkedList()

# llist.append("R")
# llist.append("A")
# llist.append("D")
# llist.append("A")
# llist.append("R")

# llist_2.append("A")
# llist_2.append("B")
# llist_2.append("C")

# llist.remove_dups_two()
# llist.print_list()
# print(llist.nth_to_last(10))
# print("-----------")
# print("    ")
# print(llist.count_occurrences(3))
# print(llist.count_occurrences_recursive(llist.head, 3))

# llist.rotate(4)
# llist.print_list()
# llist.merge_sorted_new(llist_2)
# llist.print_list()

# print("\n")
# llist.reverse_latest()
# llist.print_list()

# llist_3.remove_dups_two()
# llist_3.print_list()


# print(llist.is_palindrome())
# print(llist_2.is_palindrome())

llist.append(5)
llist.append(6)
llist.append(3)

llist_2.append(8)
llist_2.append(4)
llist_2.append(2)

# llist.print_list()
# llist.move_tail_to_head()
# print("\n")
# llist.print_list()

llist.sum_two_lists(llist_2)
print("\n")
llist.sum_two_revision(llist_2)
