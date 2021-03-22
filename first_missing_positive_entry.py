"""
FIND THE FIRST MISSING POSITIVE ENTRY

Let A be an array of length n. Design an algorithm to find 
the smallest positive integer which is not present in A. You do not 
need to preserve the contents of A.
For example, if A = [3,5,4,-1,5,1,-1],
The smallest positive integer not pesent in A is 2

1. Sorting - O(nlogn)
2. Hashtable - O(n) Space
3. If A contains k between 1 and n, we set A[k-1] to k 
   and look for i such that A[i] # i+1
   O(n) Time and O(1) Space

"""

def first_missing_positive(A):
	for i in range(len(A)):
		while 1 <= A[i] <= len(A) and A[i] != A[A[i] - 1]:
			A[A[i] - 1], A[i] = A[i], A[A[i] - 1]

    return next((i + 1 for i, a in enumerate(A) if a != i + 1), len(A) + 1)
