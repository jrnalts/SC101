"""
File: adv_permutation.py
Name:
------------------------------
This program finds all the permutations [1, 2, 3].
To complete this task, you will need backtracking
-- choose, explore, and un-choose
"""


def main():
	permutation([1, 2, 3])


def permutation(lst):
	permutation_helper(lst, [], len(lst))

	# lst = ''.join(str(e) for e in lst)
	# permutation_helper2(lst, '', len(lst))


def permutation_helper(lst, current_lst, length):
	if len(current_lst) == length:
		print(current_lst)
	else:
		for num in lst:
			if num in current_lst:
				pass
			else:
				# # Choose
				# current_lst.append(num)
				#
				# # Explore
				# permutation_helper(lst, current_lst, length)
				#
				# # Un-choose
				# current_lst.pop()

				# Another Solution
				# list + list: 記憶體位置改變，不需使用 Backtracking
				permutation_helper(lst, current_lst + [num], length)


if __name__ == '__main__':
	main()