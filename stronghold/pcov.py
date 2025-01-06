al,ans = {},[]
with open('./testcase/rosalind_pcov.txt','r') as f:
    for s in f.readlines():
        s = s.strip()
        al[u:=s[:len(s)-1]] = s[1:]
s,is_s = u,0
while not is_s or s != u:
    ans.append(u[0])
    u,is_s = al[u],1
print(''.join(ans))
