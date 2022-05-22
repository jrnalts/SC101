"""
File: l_l_append.py
Name: 
--------------------------
This file shows how to construct a linked list of mulitple numbers
"""


# It breaks the user inputs
EXIT = -1


class ListNode:
	def __init__(self, data, pointer):
		self.val = data
		self.next = pointer


def main():
	head = None

	while True:
		number = int(input('Number: '))
		if number == EXIT:
			break

		new_node = ListNode(number, None)
		if head is None:                   # First Data
			head = new_node
			cur = head
		else:
			cur.next = new_node
			cur = cur.next                 # keep cur at the last node

	traversal(head)


def traversal(head):
	"""
	:param head: ListNode, holding the first ListNode object
						   as the start of priority queue
	--------------------------
	This function prints out each val of a linked list
	"""
	cur = head
	while cur is not None:
		print(cur.val)
		cur = cur.next


if __name__ == '__main__':
	main()
