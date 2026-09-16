class LinkedList:
    class Node:
        def __init__(self, value: int, next: "LinkedList.Node | None" = None):
            self.value = value
            self.next = next

    def __init__(self):
        self.head = None
        self.tail = None
        self.members = 0

    def _getNode(self, index: int) -> "LinkedList.Node | None":
        if index < 0 or index >= self.members:
            return None
        pointer = self.head
        for i in range(index):
            pointer = pointer.next
        return pointer

    def get(self, index: int) -> int:
        node = self._getNode(index)
        if node is None:
            return -1
        else:
            return node.value

    def insertHead(self, val: int) -> None:
        self.head = self.Node(val, self.head)
        if self.tail is None:
            self.tail = self.head
        self.members += 1

    def insertTail(self, val: int) -> None:
        node = self.Node(val)
        if self.tail is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.members += 1

    def remove(self, index: int) -> bool:
        if index < 0 or index >= self.members:
            return False
        if index == 0:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
        else:
            father = self._getNode(index - 1)
            target = father.next
            father.next = target.next
            if target is self.tail:
                self.tail = father
        self.members -= 1
        return True

    def getValues(self) -> List[int]:
        arr = []
        pointer = self.head
        while pointer:
            arr.append(pointer.value)
            pointer = pointer.next
        return arr