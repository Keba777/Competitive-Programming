class Solution:
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def equationsPossible(self, equations: List[str]) -> bool:
        parent = [i for i in range(26)]
    
        for eq in equations:
            if eq[1] == "=":
                x = ord(eq[0]) - ord("a")
                y = ord(eq[3]) - ord("a")
                parent[self.find(parent, x)] = self.find(parent, y)
        
        for eq in equations:
            if eq[1] == "!":
                x = ord(eq[0]) - ord("a")
                y = ord(eq[3]) - ord("a")
                if self.find(parent, x) == self.find(parent, y):
                    return False
        
        return True
