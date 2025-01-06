with open('./testcase/rosalind_bins.txt','r') as f:
    n,m = int(f.readline()),int(f.readline())
    arr = list(map(int,f.readline().split()))
    query = list(map(int,f.readline().split()))
def f(q):
    l,r=0,n
    while l < r:
        mid = (l+r)//2
        if arr[mid] > q: r = mid
        elif arr[mid] < q: l = mid+1
        else: return mid+1
    return -1
print(*[f(q) for q in query])
