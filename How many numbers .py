class solution:
	def smallerNumbersThanCurrent(self,nums):

		sortedNums = Sorted(nums)
		dic = {}
		result = []

		for i in range(len(sortedNums)):
			if sortedNums[i] not in dic:
				dic[sortedNums[i]] = i 

		for i in nums:
			result.append(dic[i])

		return result
