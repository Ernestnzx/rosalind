with open('./testcase/rosalind_hea.txt','r') as f:
    n = int(f.readline())
    arr = list(map(int,f.readline().split()))
pq = [None]
def bubble_up(i):
    if i>>1 and pq[i>>1] < pq[i]:
        pq[i>>1],pq[i]=pq[i],pq[i>>1]
        bubble_up(i>>1)
for i in range(n): 
    pq.append(arr[i])
    bubble_up(len(pq)-1)
print(*pq[1:])
