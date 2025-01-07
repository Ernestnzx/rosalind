with open('./testcase/mass_table.txt','r') as f1:
    m = {}
    for line in f1.readlines():
        k,v=line.strip().split()
        m[k] = round(float(v)*100000)
with open('./testcase/rosalind_prsm.txt','r') as f2:
    n=int(f2.readline())
    s={}
    for _ in range(n): 
        dna = f2.readline().strip()
        s[dna] = [sum([m[c] for c in dna])]
        for i in range(1,len(dna)):
            s[dna].append(sum([m[c] for c in dna[:i]]))
            s[dna].append(sum([m[c] for c in dna[i:]]))
    r = []
    for line in f2.readlines():
        r.append(round(float(line)*100000))
    max_v,ans=0,''
    for k,v in s.items():
        mul={}
        for i in v:
            for j in r:
                if i-j not in mul: mul[i-j] = 1
                else: mul[i-j] += 1
        curr_max = max([j for i,j in mul.items()])
        if curr_max > max_v:
            max_v,ans = curr_max,k
    print(max_v)
    print(ans)