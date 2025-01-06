with open('./testcase/rosalind_mer.txt','r') as f:
    n = int(f.readline())
    a = list(map(int,f.readline().split()))
    m = int(f.readline())
    b = list(map(int,f.readline().split()))
i,j,c=0,0,[]
while i < n and j < m:
    if a[i] < b[j]: c.append(a[i]); i += 1
    else: c.append(b[j]); j += 1
while i < n: c.append(a[i]); i += 1
while j < m: c.append(b[j]); j += 1
print(*c)
