class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))
        cars.sort()  
    
        times = [(target - p) / s for p, s in cars]
        stack = []
        
        for i in range(len(cars) - 1, -1, -1):
            if not stack or times[i] > stack[-1]:
                stack.append(times[i])
            else:
                stack[-1] = max(stack[-1], times[i])
        
        return len(stack)
        
