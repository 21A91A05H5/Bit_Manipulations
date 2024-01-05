'''
Given an array of N integers, find the sum of xor of all pairs of numbers in the array arr. 
In other words, select all possible pairs of i and j from 0 to N-1 (i<j) and determine sum of all (arri xor arrj).
'''
c=0
for j in range(31,-1,-1):
    oc=zc=0
    for i in arr:
        if(i&(1<<j)):oc+=1
        else:zc+=1
    c+=(oc*zc*(1<<j))
return c
