import bisect
class SeatManager:

    def __init__(self, n: int):
        self.n = n
        self.list = [i for i in range(1,n+1)]

    def reserve(self) -> int:
        seat = self.list.pop(0) 
        return seat

    def unreserve(self, seatNumber: int) -> None:
        bisect.insort(self.list, seatNumber)
        return None
        


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)
