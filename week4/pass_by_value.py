"""
File: pass_by_value.py
Name: Jerry Liao
--------------------------
This program shows the concept of 
pass-by-value in computer memory.
"""


def main():
	print('--------------')
	a = 0
	plus_one(a)
	print(a)
	print('--------------')


def plus_one(a):
	"""
	: param a: int, the number passed from main()
	"""
	a += 1


if __name__ == '__main__':
	main()