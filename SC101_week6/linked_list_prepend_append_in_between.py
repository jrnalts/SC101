"""
File: linked_list_prepend_append_in_between.py
Name: 
--------------------------
This file shows 3 main operations on 
manipulating a linked list:
- Prepend
- Append
- In between
"""


class ListNode:
	def __init__(self, data, pointer):
		self.val = data
		self.next = pointer


def main():
	linked_list = None
	##### Construct linked_list #####
	print("Original linked_list: ")
	traversal(linked_list)
	#################################

	######## Prepend ########
	print("After prepending ('Z', 0): ")
	traversal(linked_list)
	#########################

	######## Append #########
	print("After appending ('D', 9): ")
	traversal(linked_list)
	#########################

	######### In between ############
	print("After inserting ('X', 5): ")
	traversal(linked_list)
	#################################
	

def traversal(linked_list):
	"""
	:param linked_list: ListNode, holding the first ListNode object 
						as the start of priority queue
	--------------------------
	This function prints out each val of a linked list
	"""
	cur = linked_list
	while cur is not None:
		print(cur.val)
		cur = cur.next


if __name__ == '__main__':
	main()
