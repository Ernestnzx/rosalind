from math import comb
with open('./testcase/rosalind_iprb.txt','r') as f:
    k,m,n=map(int,f.readline().split())
    t=k+m+n
    ans=(k/t)*((k-1)/(t-1))+\
        2*(k/t)*(m/(t-1))+\
        2*(k/t)*(n/(t-1))+\
        0.75*(m/t)*((m-1)/(t-1))+\
        2*0.5*(m/t)*(n/(t-1))
    print(ans)
