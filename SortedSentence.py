class Solution:
    def sortSentence(self, s: str) -> str:
        li = s.split()
        li_copy = ["a"] * len(li)
        for x in li:
            li_copy[int(x[-1])-1]=x[:-1]
        return " ".join(li_copy)
			
