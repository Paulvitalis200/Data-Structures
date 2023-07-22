# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        # split the list into two halves

        left = head
        right = self.getMid(head)
        tmp = right.next
        right.next = None

        right = tmp

        left = self.sortList(left)
        right = self.sortList(right)
        return self.merge(left, right)

    def getMid(self, head):
        slow, fast = head, head.next
        while fast and fast.next:
            slow= slow.next
            fast = fast.next.next
        return slow

    def merge(self, list1, list2):
        # tail will be the position we insert our merged node at
        # dummy allows us to avoid the edge case where we merge the two lists, the first node will be the head
        tail = dummy = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            # shift tail pointer so that we can add at the end of the list
            tail = tail.next

        if list1:
            tail.next = list1
        if list2:
            tail.next = list2

        # Return dummy.next to avoid putting the unnecessary node ListNode()
        return dummy.next

        
# Input: head = [4,2,1,3]
# Output: [1,2,3,4]