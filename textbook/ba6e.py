from Bio.Seq import Seq

def pattern_to_number(s, a='ACGT'):
    if not s: return 0
    return len(a)*pattern_to_number(s[:-1]) + a.find(s[-1])

with open('./testcase/rosalind_ba6e.txt','r') as f:
    k = int(f.readline())
    s,t = f.readline().strip(), f.readline().strip()
    n,m,c = len(s),len(t),{}
    for i in range(n-k+1):
        c.setdefault(pattern_to_number(s[i:i+k]),[]).append(i)
    for i in range(n-k+1):
        ts = t[i:i+k]; tc = str(Seq(ts).reverse_complement())
        ts,tc = pattern_to_number(ts),pattern_to_number(tc)
        if ts in c: print(*[(j,i) for j in c[ts]],sep='\n')
        if tc in c: print(*[(j,i) for j in c[tc]],sep='\n')
