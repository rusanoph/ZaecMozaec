def Z(s, N=100):
  if s < 1:
	return "Wrong parameter 's'."
  return sum([1/(n**s) for n in range(1, N)])
  
  
S = float(input())
print(Z(S))
