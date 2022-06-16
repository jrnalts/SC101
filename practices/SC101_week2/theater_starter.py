import theater


def main():
    auditorium_a = theater.Theater(5)

    print(auditorium_a.reserve())
    print(auditorium_a.reserve())
    print(auditorium_a.reserve())
    print(auditorium_a.unreserve(1))
    print(auditorium_a.unreserve(2))
    print(auditorium_a.reserve())
    print(auditorium_a.unreserve(1))
    print(auditorium_a.reserve())


if __name__ == '__main__':
    main()
