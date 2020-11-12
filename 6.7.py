def is_power(a, b):
	if a % b  == 0: 
		print (True)
		print(b, a/b)

	elif a % b != 0:
		print(False) 


is_power(2, 2)
is_power(10, 2)
is_power(1024, 8)