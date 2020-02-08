
def compute(): 

	m = 0
	for x in range(100,999): 
		for y in range(100,999): 
			z = x*y
			if (str(z) == str(z)[::-1]): 
				m = max(m,z)
	return m 

if __name__ == "__main__":
	print(str(compute()))