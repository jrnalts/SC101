def main():
    digit_sum(1729)     # 19
    digit_sum(123456)   # 21
    digit_sum(43)       # 7
    digit_sum(2300001)  # 6
    digit_sum(-1729)    # -19
    digit_sum(-7)       # -7
    digit_sum(4)        # 4
    digit_sum(0)        # 0


def digit_sum(num):
    is_negative = False
    if num < 0:
        is_negative = True
    helper(num.__abs__(), 0, is_negative)


def helper(num, sum, is_negative):
    if num == 0:
        if is_negative:
            sum *= -1
        print(sum)
    else:
        helper(num // 10, sum + num % 10, is_negative)


if __name__ == '__main__':
	main()
