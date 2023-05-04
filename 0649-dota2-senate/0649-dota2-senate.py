class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r_queue = []
        d_queue = []

        for i, ch in enumerate(senate):
            if ch == 'R':
                r_queue.append(i)
            else:
                d_queue.append(i)
                
        n = len(senate)
        while r_queue and d_queue:
            ri, di = r_queue.pop(0), d_queue.pop(0)
            if ri < di:
                r_queue.append(ri+n)
            else:
                d_queue.append(di+n)
                
        return "Radiant" if r_queue else "Dire"
