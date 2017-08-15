def is_palin(s):
	# return str(s) == str(s)[::-1]
	s = str(s)
	l = len(s)
	for i in range(l//2):
		if s[i] != s[l-i-1]:
			return False
	return True

def is_palin_str(s, match_case=False):
	if not match_case:
		s = s.lower()
	return is_palin(s)

	
if __name__ == '__main__':
	s1 = 'hola'
	s2 = 'Naman'
	print("%s = %s" % (s1,is_palin_str(s1)))
	print("%s = %s" % (s2,is_palin_str(s2)))