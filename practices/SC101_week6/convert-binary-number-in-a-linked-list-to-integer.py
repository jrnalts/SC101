# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        cur = head
        lst = []
        while cur is not None:
            lst.append(cur.val)
            cur = cur.next
        #
        # [ 1,  0,  0,  1,  0,  1 ]
        #  2^5 2^4 2^3 2^2 2^1 2^0
        #
        total = 0
        temp = 0
        for i in range(len(lst)-1, -1, -1):
            val = lst[i] * (2**temp)  # 1 * 2^0
            total += val
            temp += 1
        return total