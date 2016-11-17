def solution(A):
	zera = 0
	suma = 0
	for i in xrange(len(A)):
		if A[i] == 0:
			zera += 1
		else:
			suma += zera
	return suma

A = [0,1,0,1,1]
print(solution(A))

# nie dopilnowałem warunku, że ma zwracać -1 jeśli suma przekroczy 1KKK
# https://codility.com/demo/results/trainingS86FVV-SP8/
# 100 40 70

def solution(A):
	zera = 0
	suma = 0
	for i in xrange(len(A)):
		if A[i] == 0:
			zera += 1
		else:
			suma += zera
	if suma > 1000000000:
	    return -1
	return suma

# https://codility.com/demo/results/training3D9RCK-39R/
# 100 100 100
# O(N)