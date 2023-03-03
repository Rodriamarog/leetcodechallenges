# Given an array of integers nums and an integer target, 
# return indices of the two numbers such that they add up to target.

#input
nums = [2,7,11,15] 
target = 17

#function
def twosum():
	index = 0
	twosum = []
	for i in nums:
		j = index+1
		if j >= len(nums):
			break
		for num in range(j,len(nums)):
			if nums[index]+nums[num] == target:
				twosum.append(index)
				twosum.append(num)
				return twosum
				break
		index += 1

print(twosum())







