def isSubstring(a,b):
	''' Returns True if 'b' is a substring of 'a' '''
	return b in a
	'''
	if len(a) < len(b):
		return a in b
	else: return b in a
	'''

def isRotation(a,b):
	''' Returns True if 'b' is a rotation of 'a' '''
	return (len(a) == len(b) and isSubstring(b+b,a))

if __name__ == '__main__':
	a = "helloworld"
	b = "hello"
	c = "worldhello"

	print("a = {}, b = {}, c = {}".format(a,b,c))
	print("isSubstring(a,b) =", isSubstring(a,b))
	print("isRotation(a,c) =", isRotation(a,c))