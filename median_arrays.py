import math

# Given two sorted arrays nums1 and nums2 of size m and n respectively, 
# return the median of the two sorted arrays.

nums1 = [1,1,1]
nums2 = [2,2,2]
median = 0

nums3 = sorted(nums1 + nums2)

if len(nums3) % 2 == 1:
	median = nums3[math.floor(len(nums3)/2)]
if len(nums3) % 2 == 0:
	lwr_index = int((len(nums3)/2)-1)
	upr_index = int((len(nums3)/2))
	median = (nums3[lwr_index] + nums3[upr_index])/2

print(lwr_index)
print(upr_index)
print(median)