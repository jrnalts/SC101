class SeatManager:
    def __init__(self, n: int):
        self.total_seats = n
        self.booking_seats = []
        for i in range(n):
            self.booking_seats.append((i + 1, False))

    def reserve(self) -> int:
        reserve_num = None
        for i, seat in enumerate(self.booking_seats):
            if seat[1] == False:
                reserve_num = seat[0]
                self.booking_seats.pop(i)
                self.booking_seats.append((seat[0], True))
                break
        self.booking_seats.sort()
        return reserve_num

    def unreserve(self, seatNumber: int) -> None:
        for i, seat in enumerate(self.booking_seats):
            if seat[0] == seatNumber:
                self.booking_seats.pop(i)
            self.booking_seats.append((seat[0], False))
            break
        self.booking_seats.sort()
