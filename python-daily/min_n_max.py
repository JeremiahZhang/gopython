""" min <= n <= max, n
n < min, then min
n > max, then max 
"""

def min_max(n, _min, _max):
	return min(max(n, _min), _max)