with open('./testcase/rosalind_ba1d.txt', 'r') as f:
    s = f.readline().strip(); t = f.readline().strip()
    m,n = len(s),len(t)
    lps = [0] * m
    # KMP preprocessing algorithm
    for i in range(1, m):
        j = lps[i - 1]
        while j and s[i] != s[j]: j = lps[j - 1]
        if s[i] == s[j]: j += 1
        lps[i] = j
    # KMP search
    i=j=0; ans = []
    while i < n:
        if s[j] == t[i]:
            i += 1; j += 1
            if j == m:
                ans.append(i-m)
                j = lps[j-1]
        else:
            if j > 0: j = lps[j-1]
            else: i += 1
    print(*ans)