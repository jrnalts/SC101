"""
File: boggle.py
Name:
----------------------------------------
TODO:
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'

# Global variable
all_words = []



def main():
	"""

	"""
	start = time.time()
	####################

	read_dictionary()

	# lst = give_letters()
	lst = [['a', 'b', 'c', 'd'], ['e', 'f', 'g', 'h'], ['i', 'j', 'k', 'l'], ['m', 'n', 'o', 'p']]

	ans = []
	boggle(lst, ans)

	####################
	end = time.time()
	print('----------------------------------')
	print(f'The speed of your boggle algorithm: {end - start} seconds.')


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	with open(FILE, 'r') as f:
		for line in f:
			all_words.append(line.strip())


def boggle(lst, ans):
	for sub_idx, sub_lst in enumerate(lst):
		for ch_idx, ch in enumerate(sub_lst):
			kebab = []

			# Left
			if ch_idx != 0:
				kebab.append(lst[sub_idx][ch_idx - 1])
			# Right
			if ch_idx != 3:
				kebab.append(lst[sub_idx][ch_idx + 1])
			# Top
			if sub_idx != 0:
				kebab.append(lst[sub_idx - 1][ch_idx])
				if ch_idx != 0:
					kebab.append(lst[sub_idx - 1][ch_idx - 1])
				if ch_idx != 3:
					kebab.append(lst[sub_idx - 1][ch_idx + 1])
			# # Bottom
			if sub_idx != 3:
				kebab.append(lst[sub_idx + 1][ch_idx])
				if ch_idx != 0:
					kebab.append(lst[sub_idx + 1][ch_idx - 1])
				if ch_idx != 3:
					kebab.append(lst[sub_idx + 1][ch_idx + 1])

			boggle_helper(kebab, ans, '')


def boggle_helper(lst, ans_lst, current_str):
	# Base case
	if current_str in all_words and current_str not in ans_lst:
		ans_lst.append(current_str)
		print('Found: ' + current_str)

	# Recursive case
	else:
		for i in range(len(lst)):
			# Choose
			current_str += lst[i]

			# Explore
			if has_prefix(current_str):
				boggle_helper(lst, ans_lst, current_str)

			# Un-choose
			current_str = current_str[:-1]


def has_prefix(sub_s):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for word in all_words:
		if word.startswith(sub_s):
			return True
	return False


def give_letters():
	lst = []
	i = 1
	while True:
		if len(lst) == 4:
			break
		else:
			s = str(input(f'{i} row of letters: '))
			if len(s.replace(' ', '')) != 4 or len(s.split(' ')) != 4 or not s.replace(' ', '').isalpha():
				print('Illegal input')
				pass
			else:
				lst.append(s.split(' '))
				i += 1
	return lst


if __name__ == '__main__':
	main()
