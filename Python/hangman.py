word = input()
guess = input()
lives = 10
correct = 0
for letter in guess:
	if letter in word:
		correct += word.count(letter)
		if correct == len(word):
			print("WIN")
			break
	else:
		lives -= 1
		if lives <= 0:
			print("LOSE")
			break