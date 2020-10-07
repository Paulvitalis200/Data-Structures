class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        print('')
        print('inside function...')

        # Declare pointers for traversal.
        p1 = l1
        p2 = l2

        # Declaree current carry over
        currentCarry = 0

        # Declare cur variable to help traverse and
        # add nodes to new list.
        # Declare  head variable to be the head of the list
        head = cur = ListNode(0)

        # Iteration condition
        while p1 or p2 or currentCarry:
            print(p1.value, p2.value, currentCarry)

            currentValue = currentCarry
            currentValue += 0 if p1 is None else p1.value
            currentValue += 0 if p2 is None else p2.value
            if currentValue >= 10:
                currentValue -= 10
                currentCarry = 1
            else:
                currentCarry = 0

            print(currentValue, currentCarry)

            # Add current value as it will always at least be '1'.
            cur.next = ListNode(currentValue)
            cur = cur.next

            # Add base cases for iterating linked lists.
            if p1 is None and p2 is None:
                break
            elif p1 is None:
                p2 = p2.next
            elif p2 is None:
                p1 = p1.next
            else:
                p1 = p1.next
                p2 = p2.next

        print('exiting...')
        print('')
        return head.next

def linked_list_str(l):
    if l is None:
        return ''
    return str(l.value) + '->' + linked_list_str(l.next)

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

s = Solution()
l3 = s.addTwoNumbers(l1, l2)
print(linked_list_str(l3))