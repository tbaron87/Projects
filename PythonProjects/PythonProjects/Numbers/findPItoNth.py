# Find PI to the Nth Digit - Enter a number and have the program generate PI up to that many decimal places. Keep a limit to how far the program will go.

MAXN = 100 # The maximum n this program will search for
n = int(input("Please type which digit of PI you would like to calculate: "))

if(n > MAXN):
	print("That is higher than this program will allow!")
else:
	count = 1
	digit = 22 % 7
	while(count < n):
		digit = digit % 7
		count += 1
	print("The " + str(n) + "th digit of PI is " + str(digit))
