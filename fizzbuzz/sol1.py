for ix in range(1,101):
	if ix%3 == 0 and ix%5 == 0:
		print("FizzBuzz")
	elif ix%5 == 0:
		print("Buzz")
	elif ix%3 == 0:
		print("Fizz")
	else:
		print(ix)
