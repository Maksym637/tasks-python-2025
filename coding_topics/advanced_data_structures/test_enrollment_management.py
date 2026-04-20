import unittest

from enrollment_management import ConferenceSeating


class SolutionTests(unittest.TestCase):
    def setUp(self):
        self.cs = ConferenceSeating()

    def test_case_1(self):
        self.cs.assign_seat("Alice", "A1")
        self.assertTrue(self.cs.is_seat_assigned("A1"))
        self.assertListEqual(sorted(self.cs.list_assigned_seats()), ["A1"])
        self.assertTrue(self.cs.unassign_seat("A1"))
        self.assertFalse(self.cs.is_seat_assigned("A1"))
        self.assertListEqual(self.cs.list_assigned_seats(), [])

    def test_case_2(self):
        self.cs.assign_seat("Bob", "B1")
        self.cs.assign_seat("Charlie", "C1")
        self.cs.assign_seat("Derek", "D1")
        self.assertListEqual(sorted(self.cs.list_assigned_seats()), ["B1", "C1", "D1"])
        self.assertTrue(self.cs.is_seat_assigned("B1"))
        self.assertTrue(self.cs.is_seat_assigned("C1"))
        self.assertTrue(self.cs.is_seat_assigned("D1"))

    def test_case_3(self):
        self.cs.assign_seat("Eve", "E1")
        self.cs.assign_seat("Frank", "F1")
        self.cs.assign_seat("Grace", "G1")
        self.assertTrue(self.cs.unassign_seat("F1"))
        self.assertFalse(self.cs.is_seat_assigned("F1"))
        self.assertListEqual(sorted(self.cs.list_assigned_seats()), ["E1", "G1"])
        self.assertTrue(self.cs.unassign_seat("E1"))
        self.assertTrue(self.cs.unassign_seat("G1"))
        self.assertListEqual(self.cs.list_assigned_seats(), [])

    def test_case_4(self):
        self.cs.assign_seat("Hank", "H1")
        self.cs.assign_seat("Ivy", "H1")
        self.assertTrue(self.cs.is_seat_assigned("H1"))
        self.assertListEqual(sorted(self.cs.list_assigned_seats()), ["H1"])
        self.assertTrue(self.cs.unassign_seat("H1"))
        self.assertFalse(self.cs.is_seat_assigned("H1"))
        self.assertListEqual(self.cs.list_assigned_seats(), [])

    def test_case_5(self):
        self.cs.assign_seat("Jack", "J1")
        self.assertFalse(self.cs.unassign_seat("K1"))
        self.assertTrue(self.cs.is_seat_assigned("J1"))
        self.assertFalse(self.cs.is_seat_assigned("K1"))
        self.assertListEqual(sorted(self.cs.list_assigned_seats()), ["J1"])

    def test_case_6(self):
        long_attendee = "a" * 50
        long_seat = "s" * 50
        self.cs.assign_seat(long_attendee, long_seat)
        self.assertTrue(self.cs.is_seat_assigned(long_seat))
        self.assertListEqual(sorted(self.cs.list_assigned_seats()), [long_seat])
        self.assertTrue(self.cs.unassign_seat(long_seat))
        self.assertFalse(self.cs.is_seat_assigned(long_seat))
        self.assertListEqual(self.cs.list_assigned_seats(), [])

    def test_case_7(self):
        self.cs.assign_seat("Liam", "L1")
        self.assertFalse(self.cs.is_seat_assigned("l1"))
        self.assertListEqual(sorted(self.cs.list_assigned_seats()), ["L1"])
        self.assertTrue(self.cs.unassign_seat("L1"))
        self.assertFalse(self.cs.is_seat_assigned("L1"))
        self.assertListEqual(self.cs.list_assigned_seats(), [])


if __name__ == "__main__":
    unittest.main()
