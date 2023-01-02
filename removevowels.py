def remove_vowels(word):
	word = word.replace("a","")
	word = word.replace("e","")
	word = word.replace("i","")
	word = word.replace("o","")
	word = word.replace("u","")
	return word

print(remove_vowels(input("Tell me the word: ")))
