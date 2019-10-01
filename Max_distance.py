def maximumGap(self, A):
        size=len(A)
        if(size==1):
            return 0
        if(size==0):
            return -1
        lst=[]

        for i in range(size):

            val=A[i]
            for ele in range(size-1,i,-1):
                if(A[ele]>=val):
                    lst.append(ele-i) #
                    break
        if(len(lst)==0):
            return 0
        return max(lst)
