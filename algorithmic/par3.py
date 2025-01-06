with open('./testcase/rosalind_par3.txt','r') as f:
    n = int(f.readline())
    a = list(map(int,f.readline().split()))
    i,j,k,p=0,0,n-1,a[0]
    while j <= k:
        if a[j] < p:
            a[i],a[j]=a[j],a[i]
            i+=1;j+=1
        elif a[j] > p:
            a[j],a[k]=a[k],a[j]
            k-=1
        else:
            j+=1
    print(*a)