def maxMin(k, arr):
	"""Determine the minimum unfairness of the subarray

	Parameters
	----------
	k : int
		The number of elements to select
	arr : int[]
		An array of integers

	Return
	------
	minimum : int
		The minimum possible unfairness
	"""
	arr.sort()

	minimum = float('inf')

	for i in range(len(arr)-k+1):
		diff = arr[i+k-1] - arr[i]
		if diff < minimum:
			minimum = diff

	return minimum
