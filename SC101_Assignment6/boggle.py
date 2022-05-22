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


def main():
	"""

	"""
	start = time.time()
	####################

	lst = []
	i = 1
	while True:
		if len(lst) == 4:
			break
		else:
			s = str(input(f'{i} row of letters: '))
			if len(s.replace(' ', '')) != 4 or len(s.split(' ')) != 4:
				print('Please give 4 letters and separate with whitespace.')
				pass
			else:
				lst.append(s.split(' '))
				i += 1

	print(lst)

	####################
	end = time.time()
	print('----------------------------------')
	print(f'The speed of your boggle algorithm: {end - start} seconds.')


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	with open(FILE) as f:
		for line in f:
			dic.append(line.strip())
	return dic


def has_prefix(sub_s):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	pass


if __name__ == '__main__':
	main()
