with open('./testcase/rosalind_ba6a.txt','r') as f:
    p = eval(f.readline().strip().replace(' ',','))
    ans = []
    for i in range(len(p)):
        if p[i] == i+1: continue
        j = i
        while abs(p[j]) != i+1: j+=1
        p = p[:i]+tuple(-c for c in p[i:j+1][::-1])+p[j+1:]
        ans.append(p)
        if p[i] == -(i+1):
            p = p[:i]+tuple(-c for c in p[i:i+1][::-1])+p[i+1:]
            ans.append(p)
    print(*[f"({' '.join(f'{'+' if i > 0 else ''}{i}' for i in t)})" for t in ans], sep='\n')
