#User function Template for python3


class Solution:
    def Countpair (self, arr, n, sum) : 
        #Complete the function
        count = 0
        left = 0
        right = n - 1
        while left < right:
            if arr[left] + arr[right] == sum:
                count += 1
                left += 1
                right -= 1
            elif arr[left] + arr[right] < sum:
                left += 1
            else:
                right -= 1
        if count == 0:
            return -1
        return count
            



#{ 
 # Driver Code Starts
#Initial Template for Python 3


for _ in range(0,int(input())):
    
    n = int(input())
    arr = list(map(int,input().strip().split()))
    K = int(input())
    res = Solution().Countpair(arr, n, K)
    print(res)



# } Driver Code Ends