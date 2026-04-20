class ConferenceSeating:
    def __init__(self):
        self.assigned_seats = set()

    def assign_seat(self, attendee: str, seat: str) -> None:
        if seat not in self.assigned_seats and attendee:
            self.assigned_seats.add(seat)

    def unassign_seat(self, seat: str) -> bool:
        if seat in self.assigned_seats:
            self.assigned_seats.remove(seat)
            return True

        return False

    def is_seat_assigned(self, seat: str) -> bool:
        return seat in self.assigned_seats

    def list_assigned_seats(self) -> list[str]:
        return list(self.assigned_seats)
