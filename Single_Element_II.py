'''
Given an array of integers arr[] of length N, every element appears thrice except for one which occurs once.
Find that element which occurs once.
'''

class Solution:
    def singleElement(self, nums, N):
        def cal(num):
            c=''
            m=max(num)
            while m:
                oc=0
                for i in range(len(num)):
                    if num[i]&1:
                        oc+=1
                    num[i]>>=1
                oc=oc%3
                if oc:
                    c+='1'
                else:
                    c+='0'
                m>>=1
            return int(c[::-1],2)
        n=[]
        p=[]
        for i in nums:
                if i>=0:
                    p.append(i)
                else:
                    n.append(i*-1)
        if len(n)%3:
            return -1*cal(n)
        return cal(p)
