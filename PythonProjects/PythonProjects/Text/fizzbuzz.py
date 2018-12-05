# Fizz Buzz - Write a program that prints the numbers from 1 to 100. But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”. For numbers which are multiples of both three and five print “FizzBuzz”.

def divThree(n):
	result = False
	if(int(n) % 3 == 0):
		result = True
	return result

def divFive(n):
	result = False
	if(int(n) % 5 == 0):
		result = True
	return result

count = 1
while(count < 101):
	if(divThree(count) and divFive(count)):
		print("FizzBuzz")
	elif(divThree(count)):
		print("Fizz")
	elif(divFive(count)):
		print("Buzz")
	else:
		print(count)
	count += 1