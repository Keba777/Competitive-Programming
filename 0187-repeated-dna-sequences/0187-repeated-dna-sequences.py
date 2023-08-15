class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        sequences = {}
        result = []
        
        for i in range(len(s) - 9):
            sequence = s[i:i+10]
            sequences[sequence] = sequences.get(sequence, 0) + 1
        
        for sequence, count in sequences.items():
            if count > 1:
                result.append(sequence)
        
        return result