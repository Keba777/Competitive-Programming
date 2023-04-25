class SmallestInfiniteSet:

    def __init__(self):
        self.infinite_set = set()
        self.removed_set = set()
        self.smallest = 1

    def popSmallest(self) -> int:
        if self.smallest not in self.removed_set:
            self.removed_set.add(self.smallest)
            return self.smallest
        else:
            self.smallest += 1
            return self.popSmallest()

    def addBack(self, num: int) -> None:
        if num in self.removed_set:
            self.removed_set.remove(num)
            if num < self.smallest:
                self.smallest = num
        elif num not in self.infinite_set:
            self.infinite_set.add(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)