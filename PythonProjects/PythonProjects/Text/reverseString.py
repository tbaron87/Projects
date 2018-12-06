# Reverse a String - Enter a string and the program will reverse it and print it out.

userIn = input("Please input the string to reverse: ")
letters = []
for letter in userIn:
	letters.append(letter)
letters.reverse()
for letter in list(letters):
	print(letter)
