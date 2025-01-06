with open('./testcase/codon.txt','r') as f:
    s,d,ans = open('./testcase/rosalind_mrna.txt','r').readline().strip(),{},1
    for line in f.readlines():
        line = line.strip().split()
        for i in range(0,len(line),2):
            if line[i+1] not in d: d[line[i+1]] = 0
            d[line[i+1]] += 1
for c in s:
    ans *= d[c]
    ans %= 1000000
print((ans*d['Stop']%1000000))
