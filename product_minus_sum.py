n = 234
def substractProductAndSum(n):
	lst = []
	for i in str(n):
		lst.append(int(i))

	product = 1
	summ = 0
	for i in lst:
		product *= i
		summ += i


	result = product - summ
	return result

print(substractProductAndSum(n))