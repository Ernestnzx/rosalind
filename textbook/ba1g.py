with open('./testcase/rosalind_ba1g.txt','r') as f:
    print(sum(a!=b for a,b in zip(f.readline().strip(),f.readline().strip())))
