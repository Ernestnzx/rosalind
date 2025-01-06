from random import randint
with open('./testcase/rosalind_qs.txt','r') as f:
    n = int(f.readline())
    a = list(map(int,f.readline().split()))

def partition(i,j):
    pidx = randint(i,j)
    a[pidx],a[i]=a[i],a[pidx]
    p,m = a[i],i
    for k in range(i+1,j+1):
        if a[k] <= p: m+=1;a[k],a[m]=a[m],a[k]
    a[i],a[m]=a[m],a[i]
    return m

def quicksort(l,r):
    if l >= r: return
    p = partition(l,r)
    quicksort(l,p-1)
    quicksort(p+1,r)

quicksort(0,n-1)
print(*a)