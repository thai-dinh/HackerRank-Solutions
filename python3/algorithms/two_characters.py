from collections import Counter
from itertools import combinations

def alternate(s):
	"""Determine the longest string possible containing only two alternating letters

	Parameters
	----------
	s : str
		String

		Return
		------
	longuest : int
		Longuest string size possible containing only two alternating letters
	"""

	keys = list(Counter(list(s)).keys())
	pairs = combinations(keys, 2)
	longest = 0

	for pair in pairs:
		string = s[:]
		string = ''.join([c for c in string if c in list(pair)])
		
		current = 1
		for i in range(len(string)-1):
			if string[i] == string[i+1]:
				current = 0
				break
			else:
				current += 1

		longest = max(longest, current)

	return longest
