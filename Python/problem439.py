import math as m


# Naive implementation calculating the sum of the divisors of n. 
# This can be made to be much more efficent by using a seive to 
# find the prime factors of the original number. 

def div(N):
    global dcached
    if N in dcached: return dcached[N]
    div_sum, i = 0, 1
    q = int(math.sqrt(N))
    while i <= q:
        div_sum += (i * (N / i))
        i += 1
    i = 1
    while i <= N / (q + 1):
        m = N / i
        k = N / (i + 1)
        div_sum += (i * (m * (m + 1) - k * (k + 1)) / 2)
        i += 1
    dcached[N] = div_sum
    return div_sum
 

def S(n): 
	sum = 0
	divisorSum = 0
	computedVals = dict()

	for i in range(1,n): 
		for j in range(1,n): 
			if i*j in computedVals: 
				sum += computedVals[i*j]
		else:
			divisorSum = div(i*j)
			computedVals[i*j] = divisorSum
			sum += divisorSum

	return sum


if __name__ == "__main__": 
	print(S(3) % (10**9))

