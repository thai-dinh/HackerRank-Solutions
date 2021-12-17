def pairs(k, arr):
	"""Determine the number of pairs of array elements having their difference 
	equal to a target value.

	Parameters
	----------
	k : int
		Target value
	arr : int[]
		Array containing integers

	Return
	------
	total : int
		Number of pair having their difference equal to the target value
	"""
	dictionary = {i : i for i in arr}
	total = 0

	for num in arr:
		complement = num - k
		if complement < 0:
			continue

		if complement in dictionary:
			total += 1

	return total
	