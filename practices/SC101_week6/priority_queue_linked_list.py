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
	while True:
		name = str(input('Patient: '))  # isalpha?
		if name == EXIT:
			break
		priority = int(input('Priority: '))  # Positive?
		data = (name, priority)
		new_node = ListNode(data, None)

		if priority_queue is None:                                         # First Data
			priority_queue = new_node
		else:
			if priority < priority_queue.val[1]:                            # Prepend
				new_node.next = priority_queue
				priority_queue = new_node
			else:
				cur = priority_queue
				#####################################
				while True:
					if cur.next is None and priority >= cur.val[1]:          # Append
						cur.next = new_node
						break
					elif cur.val[1] <= new_node.val[1] < cur.next.val[1]:    # In-between
						new_node.next = cur.next
						cur.next = new_node
						break
					cur = cur.next
				#####################################

				# Other Solution
				#####################################
				while cur.next is not None:
					cur = cur.next
				if priority >= cur.val[1]:									 # Append
					cur.next = new_node
				else:
					cur = priority_queue
					while cur is not None and cur.next is not None:
						if cur.val[1] <= new_node.val[1] < cur.next.val[1]:  # In-between
							new_node.next = cur.next
							cur.next = new_node
							break
						else:
							cur = cur.next
				#####################################
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
