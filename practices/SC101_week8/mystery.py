def main():
    lst = [1, 4, 2, 7, 3]
    result = mystery(lst)

    print(result)


def mystery(lst):
    n = len(lst)

    for i in range(n-1):
        m = i
        for j in range(i+1, n):
            if lst[j] < lst[m]:
                m = j
        if m != i:
            lst[i], lst[m] = lst[m], lst[i]

    return lst


if __name__ == '__main__':
	main()