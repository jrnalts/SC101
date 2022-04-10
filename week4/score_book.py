"""
File: score_book.py
Name: 
----------------------
This program shows how to use a Python
dict by implementing a score book
"""

# This controls when to break the loop for user inputs
QUIT = ''


def main():
	"""
	This main function contains 3 functions that
	constructing a score book. d is passed by reference
	"""
	d = {}
	get_scores(d)
	check_score(d)
	print_scores(d)
	

def get_scores(d):
	"""
	: param d: (dict) an empty python dict 
	--------------------------------------
	This function puts key->value pairs in d
	"""
	print("Let's input some data!")


def check_score(d):
	"""
	: param d: (dict) a python dict contains name->score
	--------------------------------------
	This checks if key in d
	"""
	print("Let's check the score!")
	

def print_scores(d):
	"""
	: param d: (dict) a python dict contains name->score
	--------------------------------------
	This function prints out all the key-value pairs
	"""
	print('-----------------------')
	

if __name__ == '__main__':
	main()
