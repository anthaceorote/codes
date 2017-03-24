def reverse(s):
	''' Reverses given string s '''
	reversed_string = []
	for ch in reversed(s):
		reversed_string.append(ch)
	return ''.join(reversed_string)

def reverse_sentence(sentence):
	''' Reverses order of words in a sentence '''
	reversed_sentence = []
	for word in reversed(sentence.split(" ")):
		reversed_sentence.append(word)
	return ' '.join(reversed_sentence)

if __name__ == '__main__':
	a = "some_string"
	b = "this is a sentence"

	print("a = {}, b = {}".format(a,b))
	print("reverse(a) =", reverse(a))
	print("reversed_sentence(b) =", reverse_sentence(b))
	print("Reversed sentence with words reveresed =", reverse(b))