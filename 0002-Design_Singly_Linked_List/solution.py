class LinkedList:
    class Node:
        def __init__(self, value: int, next: "LinkedList.Node | None" = None):
            self.value = value
            self.next = next


    def __init__(self):
        self.head = None
        self.tail = None
        self.members = 0
    
    def _getNode(self, index: int) -> int | Node:
        if index < 0 or index > self.members-1:
            return None
        pointer = self.head
        for i in range (index):
            pointer = pointer.next
        return pointer

    def get(self, index: int) -> int:
        if index > self.members-1:
            return -1
        pointer = self.tail
        for i in range (index):
            pointer = pointer.next
        return pointer.value

    def insertHead(self, val: int) -> None:
        if self.head is None:
            self.head = self.Node(val)
            if self.tail is None:
                self.tail = self.head
        else:
            self.head.next = self.Node(val)
            self.head = self.head.next
        self.members += 1

    def insertTail(self, val: int) -> None:
        if self.tail is None:
            self.tail = self.Node(val)
            if self.head is None:
                self.head = self.tail
        else:
            self.tail = self.Node(val, self.tail)
        self.members += 1
        
    def remove(self, index: int) -> bool:
        if index > self.members-1:
            return False
        if index == 0:
            if self.members == 2:
                self.tail = self.head
                self.members -= 1
                return True
            elif self.members == 1:
                self.tail = None
                self.head = None
                self.members = 0
                return True
            else:
                self.tail = self.tail.next
                self.members -= 1
                return True
                
        father = self._getNode(index-1)
        target = father.next
        if target.next is None:
            father.next = None
            self.head = father
        else:
            father.next = target.next
        
        self.members -= 1
        return True
        

    def getValues(self) -> List[int]:
        arr = []
        pointer = self.tail
        if pointer is None:
            return []
        while True:
            arr.append(pointer.value)
            if pointer.next is None:
                break
            else:
                pointer = pointer.next
        return arr[::-1]
