ans = []
def perm(a,n,c):
    if c == n-1:
        ans.append(a.copy())
        return
    for i in range(c,n):
        a[c],a[i]=a[i],a[c]
        perm(a,n,c+1)
        a[c],a[i]=a[i],a[c]

n = int(open('./testcase/rosalind_perm.txt','r').readline())
perm([i for i in range(1,n+1)],n,0)
print(len(ans))
for i in range(len(ans)):
    for j in ans[i]:
        print(j,end=' ')
    print()
