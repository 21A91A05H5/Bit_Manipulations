#User function Template for python3

class Solution:
    #Complete this function
    # Function for finding maximum AND value.
    def maxAND(self, arr,N):
        #Your code here
        x=max(arr)
        #arr=list(set(arr))
        k=0
        while x:
            k+=1
            x>>=1
        res=0
        x=max(arr)
        while (x):
            c=0
            a=[]
            i=0
            while i<len(arr):
                if arr[i]&(1<<k):
                    c+=1
                    a.append(arr[i])
                i+=1
            if c>1:
                arr=a
                res+=(1<<k)
            x>>=1
            k-=1
        c=0
        a=[]
        i=0
        while i<len(arr):
            if arr[i]&(1<<k):
                c+=1
                a.append(arr[i])
            i+=1
        if c>1:
            arr=a
            res+=(1<<k)
        return res
