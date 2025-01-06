from random import randint
def partition(i,j):
    pidx = randint(i,j)
    a[pidx],a[i]=a[i],a[pidx]
    p,m = a[i],i
    for k in range(i+1,j+1):
        if a[k] <= p: m+=1;a[k],a[m]=a[m],a[k]
    a[i],a[m]=a[m],a[i]
    return m

def select(l,r,k):
    if l == r: return a[l]
    p = partition(l,r)
    if p == k-1:
        return a[p]
    elif k-1 < p:
        return select(l,p-1,k)
    else:
        return select(p+1,r,k)

with open('./testcase/rosalind_med.txt','r') as f:
    n=int(f.readline())
    a=list(map(int,f.readline().split()))
    k=int(f.readline())
print(select(0,n-1,k))