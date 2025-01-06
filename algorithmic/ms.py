with open('./testcase/rosalind_ms.txt','r') as f:
    n = int(f.readline())
    arr = list(map(int,f.readline().split()))
def merge_sort(l,r):
    if l >= r: return
    mid = (l+r)//2
    merge_sort(l,mid)
    merge_sort(mid+1,r)
    temp = [0]*(r-l+1)
    idx,idxl,idxr=0,l,mid+1
    while idxl <= mid and idxr <= r:
        if arr[idxl] <= arr[idxr]: 
            temp[idx]=arr[idxl]
            idx+=1;idxl+=1
        else:
            temp[idx]=arr[idxr]
            idx+=1;idxr+=1
    while idxl <= mid: temp[idx]=arr[idxl];idx+=1;idxl+=1
    while idxr <= r: temp[idx]=arr[idxr];idx+=1;idxr+=1
    for i in range(l,r+1): arr[i] = temp[i-l]
merge_sort(0,n-1)
print(*arr)
