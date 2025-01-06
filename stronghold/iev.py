with open('./testcase/rosalind_iev.txt','r') as f:
    a,b,c,d,e,f=map(int,f.readline().split())
    print(2*(a+b+c+0.75*d+0.5*e))
