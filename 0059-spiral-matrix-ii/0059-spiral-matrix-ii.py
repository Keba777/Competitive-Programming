class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0 for _ in range(n)] for _ in range(n)]

        count = 1
        for layer in range((n + 1) // 2):
            # Traverse right
            for i in range(layer, n - layer):
                matrix[layer][i] = count
                count += 1

            # Traverse down
            for i in range(layer + 1, n - layer):
                matrix[i][-(layer + 1)] = count
                count += 1

            # Traverse left
            for i in range(layer + 1, n - layer):
                matrix[-(layer + 1)][-(i + 1)] = count
                count += 1

            # Traverse up
            for i in range(layer + 1, n - layer - 1):
                matrix[-(i + 1)][layer] = count
                count += 1

        return matrix
