def number_to_pattern(i,k,a='ACGT'):
    if k == 0: return ''
    return number_to_pattern(i//len(a),k-1) + a[i%len(a)]

with open('./testcase/rosalind_ba2b.txt','r') as f:
    k,dna = int(f.readline()),[s.strip() for s in f.readlines()]
    max_d,median = 10**9,''
    for i in range(4**k):
        s,d = number_to_pattern(i,k),0
        for t in dna:
            n,hd = len(t),10**9
            for j in range(n-k+1):
                hd = min(hd,sum(a!=b for a,b in zip(s,t[j:j+k])))
            d += hd
        if d < max_d: max_d,median = d,s
    print(median)
