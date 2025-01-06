with open('./testcase/rosalind_par.txt','r') as f:
    n = int(f.readline())
    a = list(map(int,f.readline().split()))
def partition(i,j):
    p,m = a[i],i
    for k in range(i+1,j+1):
        if a[k] <= p: m+=1;a[k],a[m]=a[m],a[k]
    a[i],a[m]=a[m],a[i]
    return m
partition(0,n-1)
print(*a)
