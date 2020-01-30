#Python Solution
class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def diagonal(self, A):
        B=[]
        for k in range(len(A)):
            B.append([])
            i=0
            j=k
            while(j>=0):
                B[k].append(A[i][j])
                i+=1
                j-=1
        for L in range(1,len(A)):
            B.append([])
            i=L
            j=len(A)-1
            while(i<len(A)):
                B[k+L].append(A[i][j])
                i+=1
                j-=1
        return B
