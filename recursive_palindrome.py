
#function to recursively check if a word is a palindrome
def recur_palindrome(word):
	if len(word) < 2:
		return True
	elif word[0] == word[-1]:
		return recur_palindrome(word[1:-1])
	else:
		return False
