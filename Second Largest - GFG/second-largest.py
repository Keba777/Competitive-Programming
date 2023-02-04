#User function Template for python3
class Solution:

	def print2largest(self,arr, n):
		# code here
		max1 = -1000000
		max2 = -1000000
		for i in range(n):
		    if arr[i] > max1:
		        max2 = max1
		        max1 = arr[i]
		        
	        elif arr[i] > max2 and arr[i] != max1:
	            max2 = arr[i]
	            
	    if max2 == -1000000:
	        return -1
	    else:
	        return max2
		    


#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.print2largest(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends