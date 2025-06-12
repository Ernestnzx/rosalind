def pattern_to_number(s, a='ACGT'):
    if not s: return 0
    return 4*pattern_to_number(s[:-1]) + a.find(s[-1])

with open('./testcase/rosalind_ba1k.txt','r') as f:
    s,k = f.readline().strip(),int(f.readline())
    n,arr = len(s),[0]*4**k
    for i in range(n-k+1):
        arr[pattern_to_number(s[i:i+k])]+=1
    print(*arr)