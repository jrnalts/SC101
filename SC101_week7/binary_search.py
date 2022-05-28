def main():
	lst = [3, 6, 9, 10, 11, 23, 33, 45, 66, 99]
	print(binary_search(lst, 7))
	print(binary_search(lst, 23))


def binary_search(lst, target):
	"""
	:param lst: list[int], a Python list storing integers.
	:param target: int, the value to be searched.
	:returns : bool, if target is in the lst or not.
	"""
	# Your Code Here
	mid_i = len(lst) // 2
	return helper(lst, target, mid_i)


def helper(lst, target, mid_i):
	if target == lst[mid_i]:
		return True
	else:
		if target > lst[mid_i]:
			new_lst = lst[mid_i+1:]
		else:
			new_lst = lst[:mid_i]

		if len(new_lst) == 0:
			return False

		mid_i = len(new_lst) // 2
		return helper(new_lst, target, mid_i)


if __name__ == '__main__':
	main()
