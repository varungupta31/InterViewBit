def maximumGap(self, A):
       n=len(A)
       if(n==0):
           return -1
       if(n==1):
           return 0
       lst=[]
       for i in range(n):
           lst.append([A[i],i])
       lst.sort()
       ans=0
       rmax=lst[n-1][1]
       for i in range(n-2,-1,-1):
           ans=max(ans,rmax-lst[i][1])
           rmax=max(rmax,lst[i][1])
       return ans
