# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def delete_duplicates(self, head):
        cur = head
        d = {}
        while cur is not None:
            key = cur.val
            if key in d:
                d[key] += 1
            else:
                d[key] = 1
            cur = cur.next

        # Solution 1
        # head = None
        # for val, count in d.items():
        #     if count == 1:
        #         if head is None:
        #             head = ListNode(val)
        #             cur = head
        #         else:
        #             cur.next = ListNode(val)
        #             cur = cur.next
        # return head

        # Solution 2
        dummy = ListNode()
        cur = dummy
        for val, count in d.items():
            if count == 1:
                cur.next = ListNode(val)
                cur = cur.next
        return dummy.next


def main():
    # give example
    lst = [1, 2, 3, 3, 4, 4, 5]
    dummy = ListNode()
    cur = dummy
    for n in lst:
        new_node = ListNode(n, None)
        cur.next = new_node
        cur = cur.next

    obj = Solution()
    result = obj.delete_duplicates(dummy.next)
    traversal(result)


def traversal(linked_list):
    cur = linked_list
    while cur is not None:
        print(cur.val, end=', ')
        cur = cur.next


if __name__ == '__main__':
    main()