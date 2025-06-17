with open('./testcase/rosalind_ba3l.txt','r') as f:
    k,d = map(int,f.readline().split())
    a,b = [],[]
    for s in f.readlines():
        i,j = s.strip().split('|')
        a.append(i); b.append(j)
    prefix = a[0] + ''.join(a[i][-1] for i in range(1,len(a)))
    suffix = b[0] + ''.join(b[i][-1] for i in range(1,len(b)))
    n,m = len(prefix),len(suffix)
    assert all(prefix[i] == suffix[i-k-d] for i in range(k+d+1,n))
    print(prefix + suffix[m-k-d:m])
