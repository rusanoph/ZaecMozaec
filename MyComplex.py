import matplotlib.pyplot as plt

class MyComplex:
	def __init__(self, Re, Im):
		self.Re = Re
		self.Im = Im


	def __add__(self, other):
		new_Re = self.Re + other.Re
		new_Im = self.Im + other.Im
		return MyComplex(new_Re, new_Im)


	def __iadd__(self, other):
		return self.__add__(other)


	def __mul__(self, other):
		new_Re = self.Im * other.Re + self.Re * other.Im
		new_Im = self.Re * other.Re - self.Im * other.Im
		return MyComplex(new_Re, new_Im)


	def __imul__(self, other):
		return self.__mul__(other)


	def __eq__(self, other):
		return (self.Re == other.Re) and (self.Im == self.Im)


	def __radd__(self, other):
		return MyComplex(0, 0)


	def __str__(self):
		if self.Im >= 0:
			return f'{self.Re} + j{self.Im}'
		else:
			return f'{self.Re} - j{-self.Im}'


n = 4
z = MyComplex(1, 1)
S = []

for i in range(1, n):
	for j in range(1, n):
		z *= MyComplex(i, j)
		S.append(z)

S_Re = [z.Re for z in S]
S_Im = [z.Im for z in S]

plt.plot(S_Re, S_Im)
plt.show()