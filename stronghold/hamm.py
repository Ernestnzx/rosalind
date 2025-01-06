with open('./testcase/rosalind_hamm.txt','r') as f:
    s = f.readline().strip()
    t = f.readline().strip()
    n,ans=len(s),0
    for i in range(n):
        ans += s[i] != t[i]
    print(ans)
