# Definition for singly-
# LeetCode # 234


# It breaks the user inputs
EXIT = -1


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def main():
    head = None
    while True:
        number = int(input('Number: '))
        if number == EXIT:
            break
        new_node = ListNode(number, None)
        if head is None:  # First Data
            head = new_node
            cur = head
        else:
            cur.next = new_node
            cur = cur.next  # keep cur at the last node

    cur = head
    lst = []
    while cur is not None:
        lst.append(cur.val)
        cur = cur.next

    ##################################
    # Solution with for loop
    # for i in range(len(lst) // 2):
    #     if lst[i] != lst[-1 - i]:
    #         return False
    # return True

    ##################################
    # Solution with recursion
    print(is_palindrome_helper(lst))


def is_palindrome_helper(lst):
    if len(lst) == 1 or len(lst) == 0:
        return True
    else:
        if lst[0] != lst[-1]:
            return False
        else:
            return is_palindrome_helper(lst[1:len(lst) - 1])


if __name__ == '__main__':
    main()
