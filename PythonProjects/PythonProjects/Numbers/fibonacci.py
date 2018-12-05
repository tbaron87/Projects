# Fibonacci Sequence - Enter a number and have the program generate the Fibonacci sequence to that number or to the Nth number.

def recursiveFib(n):
	num = 0
	if(int(n) == 1):
		num = 1
	elif(int(n) > 1):
		num = recursiveFib(n - 1) + recursiveFib(n - 2)
	return num

n = input("Please input the Fibonacci number you would like: ")

print("The result is: " + str(recursiveFib(int(n) - 1))) # n - 1 because the first number is 0
