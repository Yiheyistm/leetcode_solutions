class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        min_move = 0
        for seat, stud in zip(seats, students):
            min_move += abs(seat - stud)
        return min_move
        