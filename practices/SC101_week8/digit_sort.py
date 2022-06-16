def main():
    digit_sorted(0)         # True
    digit_sorted(2345)      # True
    digit_sorted(-2345)     # True
    digit_sorted(22334455)  # True
    digit_sorted(-5)        # True
    digit_sorted(4321)      # False
    digit_sorted(24378)     # False
    digit_sorted(21)        # False
    digit_sorted(-33331)    # False


def digit_sorted(num):
    helper(num.__abs__())


def helper(num):
    if num <= 1:
        # print(True)
        return True
    else:
        cur = num % 10
        last = (num // 10) % 10
        if cur < last:
            # print(False)
            return False
        else:
            return helper(num // 10)


if __name__ == '__main__':
	main()
