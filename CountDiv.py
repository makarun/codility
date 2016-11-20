# ze zlozonoscia O(N)
def solution(A, B, K):
	divs = 0
	if A == 0 and B == 0:
	    return 0
	for i in range(A,B+1):
		if i % K == 0:
			divs += 1
	return divs

print(solution(6,11,2))


# https://codility.com/demo/results/trainingXEJ5AC-27U/
# 75 0 37
# O(B-A)

def solution(A, B, K):
    if A % K == 0:
        return(B-A) // K+1
    else:
        return(B-(A-A%K))//K

# https://codility.com/demo/results/trainingMUTT2G-GQQ/
# 100 100 100
# O(1)