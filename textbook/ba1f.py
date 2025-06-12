with open('./testcase/rosalind_ba1f.txt','r') as f:
    s,a,min_a,ans = f.readline().strip(),0,0,[0]
    for i,c in enumerate(s):
        if c == 'A' or c == 'T': continue
        a += 1 if c == 'G' else -1
        if a <= min_a:
            if a < min_a: ans.clear()
            min_a = a; ans.append(i+1)
    print(*ans)
