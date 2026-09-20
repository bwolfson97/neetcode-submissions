class DynamicArray:
    
    def __init__(self, capacity: int):
        self.arr = [None] * capacity
        self.size = 0

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        if self.getSize() == self.getCapacity():
            self.resize()
        self.set(self.getSize(), n)
        self.size += 1

    def popback(self) -> int:
        self.size -= 1
        return self.get(self.getSize())

    def resize(self) -> None:
        self.arr = self.arr + [None] * len(self.arr)

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return len(self.arr)
