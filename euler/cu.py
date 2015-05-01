def sumInArray(arr, total):
	numbers = [{"a":a,"b":b} for a in arr for b in arr]
	results = []
	for number in numbers:
		if number["a"] + number["b"] == total:
			print number
		# print results

sumInArray([2,5,3,7,9,8],11)