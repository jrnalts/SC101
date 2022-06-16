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


def main(head):
    if head is None:
        return head
    else:
        head_lst = []
        tail_lst = []
        cur = head

    while cur.next is not None:
        if cur.val < x:
            head_lst.append(cur.val)
        else:
            tail_lst.append(cur.val)
            cur = cur.next
        final_lst = head_lst + tail_lst
        dummy = ListNode()
        cur = dummy.next
        for val in final_lst:
            cur = ListNode(val)
            cur = cur.next

    return dummy.next

    if head is None:
        return head
    else:
        dummy = dummy2 = ListNode()
        new_head = dummy.next
        tail = dummy2.next

        front_cur = new_head  # 裝 < x 的
        tail_cur = tail  # 裝 >= x 的

    cur = head
    while cur is not None:
        if cur.val < x:
            front_cur.next = cur.val
            front_cur = front_cur.next
        else:
            tail_cur.next = cur.val
            tail_cur = tail_cur.next
        cur = cur.next

    cur = new_head
    while cur is not None:
        if cur.next is None:  # 最後一顆 Node
            cur.next = tail  # 接上 tail

    return new_head

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