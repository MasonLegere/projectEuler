import problem3


def calc():
	counter = 1
	x = 2 
	while counter < 10001:
		x +=1 
		if problem3.is_Prime(x):
			counter +=1
	return x
if __name__ == "__main__":
	print(calc())

	
