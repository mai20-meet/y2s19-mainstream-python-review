def encode(x, y):
	if 1<y and y<250 and x>500 and x<1000:
		return(x*y)
	print("Invalid input: Outside range.")
	return None
encode(2,2)

def is_prime(x,y):
	while x%2==1:
		x+=1
	while y%2==1:
		y+=1
	if 1<y and y<250 and x>500 and x<1000:
		return(x*y)
	print("Invalid input: Outside range.")
	return None
is_prime(3,3)

def decode(coded_message):
	# input : coded_message
	# output : x,y
	# x*y = coded_message
	# y = coded_message/x
	for i in range(2, 250):
		print(y)
		if not is_prime(y):
			continue
	#make sure x is also an integer 
		if coded_message%y == 0:
			x = coded_message / y
			if (is_prime(int(x)) and 500 < x < 1000):
				return (x, y)
