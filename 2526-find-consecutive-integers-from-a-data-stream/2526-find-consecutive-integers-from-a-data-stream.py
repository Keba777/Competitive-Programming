class DataStream:

    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.queue = deque()
        self.count = 0

    def consec(self, num: int) -> bool:
        self.queue.append(num)
        if num == self.value:
            self.count += 1
            
        if len(self.queue) < self.k:
            return False

        if len(self.queue) > self.k:
            if self.value == self.queue[0]:
                self.count -= 1

            self.queue.popleft()

        if self.k == self.count:
            return True
        return False
    


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)