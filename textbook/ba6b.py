with open('./testcase/rosalind_ba6b.txt','r') as f:
    p = eval(f.readline().strip().replace(' ',','));
    print((p[0]!=1)+(p[-1]!=len(p))+sum(abs(p[i]-p[i-1])!=1 for i in range(1,len(p))))
