"""
File: subsets.py
Name:
-------------------------
This file prints all the sub-lists on Console
by calling a recursive function - list_sub_lists(lst).
subsets.py is a famous LeetCode Medium problem
"""


def main():
    """
    LeetCode Medium Problem
    """
    list_sub_lists([1, 2, 3, 4])


def list_sub_lists(lst):
    """
    :param lst: list[str], containing a number of characters
    """
    helper(lst, [], 0)


def helper(lst, current_lst, current_i):
    print(current_lst)
    for i in range(current_i, len(lst)):
        # Choose
        current_lst.append(lst[i])

        # Explore
        helper(lst, current_lst, i+1)

        # Un-choose
        current_lst.pop()


if __name__ == '__main__':
    main()
