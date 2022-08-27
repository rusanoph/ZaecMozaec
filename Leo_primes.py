def prime(n):
	number = 2
	primes = []

	while n > len(primes):
		for p in primes:
			if number % p == 0:
				break
		else:
			primes.append(number)
		number += 1

	return primes


def primorial(n):
	if n <= 1:
		return 0

	prod = 1
	for p in prime(n):
		prod *= p

	return prod


n = list(map(int, input().split()))
k = 0

for d in n:
	while d > primorial(k):
		k += 1

	print(k - 1) 