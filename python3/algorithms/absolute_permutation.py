def absolutePermutation(n, k):
	"""Compute the smallest lexicographically absolute permutation.

	Parameters
	----------
	n : int
		Upper bound of natural numbers to consider, inclusive
	k : int
		Absolute difference between each element's value and its index

	Return
	------
	result : int[]
		Smallest lexicographically permutation, or [-1] if there is none
	"""

	result = []
	indexes = set([i for i in range(1, n+1)])
	
	for i in range(1, n+1):
		pos1 = k + i
		pos2 = i - k if i - k >= 1 else pos1

		mini = min(pos1, pos2)
		maxi = max(pos1, pos2)

		if mini in indexes:
			result.append(mini)
			indexes.remove(mini)
		elif maxi in indexes:
			result.append(maxi)
			indexes.remove(maxi)
		else:
			return [-1]

	return result
