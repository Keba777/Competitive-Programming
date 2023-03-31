from bisect import bisect
class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.leaders = []
        self.times = times
        self.leader_tracker = {}
        current_leader = -1

        for p in persons:
            self.leader_tracker[p] = self.leader_tracker.get(p, 0) + 1
            if self.leader_tracker[p] >= self.leader_tracker.get(current_leader, 0):
                current_leader = p
            self.leaders.append(current_leader)
        

    def q(self, t: int) -> int:
        index = bisect(self.times, t)
        if index == len(self.leaders): 
            return self.leaders[-1]
        return self.leaders[index - 1]
        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
