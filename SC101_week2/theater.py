class Theater:
    # Your Code Here
    def __init__(self, n):
        self.total_seats = n
        self.booking_seats = []
        for i in range(n):
            self.booking_seats.append((i + 1, False))

    def reserve(self):
        reserve_num = None
        for i, seat in enumerate(self.booking_seats):
            if seat[1] == False:
                reserve_num = seat[0]
                self.booking_seats.pop(i)
                self.booking_seats.append((seat[0], True))
                break

        self.booking_seats = sorted(self.booking_seats)
        return reserve_num

    def unreserve(self, seat_number):
        for i, seat in enumerate(self.booking_seats):
            if seat[0] == seat_number:
                self.booking_seats.pop(i)
                self.booking_seats.append((seat[0], False))
                break

        self.booking_seats = sorted(self.booking_seats)
