with open('./testcase/rosalind_ins.txt','r') as f:
    n,ans = int(f.readline()),0
    arr = list(map(int,f.readline().split()))
    for i in range(1,n):
        k = i
        while k and arr[k] < arr[k-1]:
            arr[k],arr[k-1]=arr[k-1],arr[k]
            k-=1;ans+=1
    print(ans)
