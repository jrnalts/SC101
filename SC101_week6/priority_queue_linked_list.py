"""
File: priority_queue_linked_list.py
Name: 
--------------------------
This file shows how to construct a linked list 
from scratch and use it to implement a priority queue.
"""


# It breaks the user inputs
EXIT = ''


class ListNode:
	def __init__(self, data, pointer):
		self.val = data
		self.next = pointer


def main():
	priority_queue = None
	
	print('--------------------------------')
	# TODO:
	print('--------------------------------')
	traversal(priority_queue)


def traversal(priority_queue):
	"""
	:param priority_queue: ListNode, holding the first ListNode object 
						   as the start of priority queue
	--------------------------
	This function prints out each val of a linked list
	"""
	cur = priority_queue
	while cur is not None:
		print(cur.val)
		cur = cur.next


if __name__ == '__main__':
	main()
