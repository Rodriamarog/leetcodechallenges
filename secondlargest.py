def second_largest(nums):
	nums.remove(max(nums))
	return max(nums)

nums = []
for i in range(3):
	nums.append(int(input("Tell me the nums: ")))

print(second_largest(nums))