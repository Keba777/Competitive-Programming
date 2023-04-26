class MyCircularDeque:
    def __init__(self, k: int):
        self.deque = [None] * k
        self.front = 0
        self.rear = 0
        self.size = 0
        self.capacity = k

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.front = (self.front - 1) % self.capacity
        self.deque[self.front] = value
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.deque[self.rear] = value
        self.rear = (self.rear + 1) % self.capacity
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.deque[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.rear = (self.rear - 1) % self.capacity
        self.deque[self.rear] = None
        self.size -= 1
        return True

    def getFront(self) -> int:
        return -1 if self.isEmpty() else self.deque[self.front]

    def getRear(self) -> int:
        return -1 if self.isEmpty() else self.deque[(self.rear - 1) % self.capacity]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity


# # Your MyCircularDeque object will be instantiated and called as such:
# # obj = MyCircularDeque(k)
# # param_1 = obj.insertFront(value)
# # param_2 = obj.insertLast(value)
# # param_3 = obj.deleteFront()
# # param_4 = obj.deleteLast()
# # param_5 = obj.getFront()
# # param_6 = obj.getRear()
# # param_7 = obj.isEmpty()
# # param_8 = obj.isFull()
