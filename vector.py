def vector_add(v,w):
	"""adds corresponding elements"""
	return [v_i + w_i for v_i, w_i in zip(v,w)]

def vector_subtract(v,w):
	"""subtracts corresponding elements"""
	return [v_i - w_i for v_i, w_i in zip(v,w)]

def vector_sum(vectors):
	"""sums all corresponding elements"""
	result = vectors[0]
	for vector in vectors[1:]:
		result = vector_add(result, vector)
	return result
	### return reduce(vector_add, vectors)

def scalar_multiply(c,v):
	""" c number, v vector"""
	return [c*v_i for v_i in v]

def vector_mean(vectors):
	"""compute the vector whose ith element is the mean of the ith element of the input vectors"""
	n = len(vectors)
	return scalar_multiply(1/n, vector_sum(vectors))

def dot(v,w):
	"""v_1*w_1 + ... + v_n*w_n"""
	return sum(v_i * w_i for v_i, w_i in zip(v,w))

def sum_of_squares(v):
	"""v_1*v_1 + ... + v_n * v_n"""
	return dot(v, v)

import math
def magnitude(v):
	return math.sqrt(sum_of_squares(v))

def distance(v,w):
	return magnitude(vector_subtract(v,w))

""" Use Numpy library for high performance array calss with all sorts of arithmetic operations """