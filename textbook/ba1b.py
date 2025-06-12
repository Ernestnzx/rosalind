with open('./testcase/rosalind_ba1b.txt','r') as f:
    s = f.readline().strip(); n = int(f.readline())
    kmer = {}
    for i in range(len(s)-n):
        t = s[i:i+n]
        if t not in kmer: kmer[t] = 0
        kmer[t] += 1
    ans = sorted(kmer.items(),key=lambda x : -x[1])
    print(*map(lambda x : x[0], filter(lambda x : x[1] == ans[0][1],ans)))