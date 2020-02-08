# The standard naive implementation would have have been more efficient 
# as the total needs to be recorded sequentially. However, this was
# more interesting and based on better math.


def compute(): 
	return str(sum(fibonacci(x) for x in range((10**4)) if fibonacci(x) % 2 == 0 and fibonacci(x) < 4*(10**6)))

def fibonacci(n):
	if n < 0:
		raise ValueError("Negative arguments not implemented")
	return _fib(n)[0]

def _fib(n): 
	if n == 0: 
		return (0,1)
	else: 
		a, b = _fib(n // 2)
		c = a * (b * 2 - a)
		d = a * a + b * b
		if n % 2 == 0:
			return (c, d)
		else:
			return (d, c + d)

if __name__ == "__main__": 
	print(compute())


