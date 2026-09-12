class DynamicArray:

    def __init__(self, capacity: int):
        self.values = [None]*capacity
        self.vacant = 0
        self.capacity = capacity

    def get(self, i: int) -> int:
        return self.values[i]

    def set(self, i: int, n: int) -> None:
        if self.values[i] is None:
            self.vacancy += 1
        self.values[i] = n

    def pushback(self, n: int) -> None:
        if self.vacant == self.capacity:
            self.resize()
        self.values[self.vacant] = n
        self.vacant += 1 

    def popback(self) -> int:
        target = self.vacant - 1
        returnValue = self.values[target]
        self.values[target] = None
        self.vacant -= 1
        return returnValue

    def resize(self) -> None:
        new = [None]*self.capacity*2
        for i in range(len(self.values)):
            new[i] = self.values[i]
        self.values = new
        self.capacity = self.capacity*2

    def getSize(self) -> int:
        return self.vacant
    
    def getCapacity(self) -> int:
        return len(self.values)
