"""
File: largest_digit.py
Name:
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n: (Integer): number for check.
 	:return: (Integer): The largest digit.
	"""
	# Helper only accept positive value and get last digit form n
	return find_largest_digit_helper(abs(n), abs(n) % 10)


def find_largest_digit_helper(current_n, largest):
	if current_n % 10 >= largest:  # Compare digit value
		largest = current_n % 10

	if current_n // 10 == 0:  # Last Digit
		return largest
	else:
		return find_largest_digit_helper(current_n // 10, largest)


if __name__ == '__main__':
	main()
