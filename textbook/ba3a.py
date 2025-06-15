with open('./testcase/rosalind_ba3a.txt','r') as f:
    k = int(f.readline())
    s = f.readline().strip()
    print(*sorted([s[i:i+k] for i in range(len(s)-k+1)]),sep='\n')