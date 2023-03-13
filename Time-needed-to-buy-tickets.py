class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        n = len(tickets)
        sold = [0] * n
        time = 0
        
        while sold[k] < tickets[k]:
            for i in range(n):
                if tickets[i] > sold[i]:
                    sold[i] += 1
                    time += 1
                    if i == k and sold[k] == tickets[k]:
                        return time
        return time
        

                    
