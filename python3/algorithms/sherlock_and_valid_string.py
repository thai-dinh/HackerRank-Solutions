def isValid(s):
	"""Determine if the given string is valid according to Sherlock

	Parameters
	----------
	s : str
		String

	Return
	------
	response : str
		'YES' if it is a valid string else 'NO'
	"""

	chars = list(s)
	freq = {}
	occ = {}
	
	for c in chars:
		freq[c] = freq.get(c, 0) + 1
	
	for v in freq.values():
		occ[v] = occ.get(v, 0) + 1

	if len(occ) > 2:
		return 'NO'

	if len(occ) == 2:
		occ = dict(sorted(occ.items(), key=lambda x: x[1]))

		val1 = list(occ.values())[0]
		key1 = list(occ.keys())[0] - 1
		key2 = list(occ.keys())[1]

		if not(val1 == 1 and (key1 == key2 or key1 == 0)):
			return 'NO'

	return 'YES'
