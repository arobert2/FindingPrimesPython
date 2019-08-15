Numbers = 100

primes = [2]
isprime = True


for x in range(3,100):
	for d in primes:
		if x % d == 0:
			isprime = False
	if isprime:
		primes.append(x)
		print(x)
	isprime = True

