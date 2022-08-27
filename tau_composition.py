import matplotlib.pyplot as plt
import math


def tau(n):
	divisors = 1
	N = int(math.sqrt(n))

	for d in range(2, N + 1):
		if n % d == 0:
			divisors += 2
		if d == N:
			divisors -= 1

	return divisors + 1


def tau_comps(n):
	comp = 0
	while n != 2:
		n = tau(n)
		comp += 1

	return comp


N = 10**5
X = [x for x in range(2, N + 2)]
Y = [2.71**tau_comps(x) for x in X]
Y_log = [math.log(x) for x in X]

plt.plot(X, Y)
plt.plot(X, Y_log)
plt.grid()
plt.xscale('log')
plt.show()