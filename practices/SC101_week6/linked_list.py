"""
File: linked_list.py
Name: 
--------------------------
This file shows how to construct a linked list 
from scratch and use it to implement a priority queue.
"""


class ListNode:
	def __init__(self, data, pointer):
		self.val = data
		self.next = pointer


def main():

	# Reverse linking
	node3 = ListNode(('C', 7), None)
	node2 = ListNode(('B', 5), node3)
	node1 = ListNode(('A', 3), node2)

	# Forward linking
	node1 = ListNode(('A', 3), None)
	node2 = ListNode(('B', 5), None)
	node3 = ListNode(('C', 7), None)
	node1.next = node2
	node2.next = node3

	# Set data structure as first node
	linked_list = node1

	# Print nodes of linked list
	traversal(linked_list)


def traversal(linked_list):
	cur = linked_list
	# while True:
	# 	if cur.next is not None:
	# 		print(cur.val)
	# 		cur = cur.next
	# 	else:
	# 		print(cur.val)
	# 		break
	while cur is not None:
		print(cur.val)
		cur = cur.next


if __name__ == '__main__':
	main()
