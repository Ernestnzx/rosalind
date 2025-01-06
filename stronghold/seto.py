with open('./testcase/rosalind_seto.txt','r') as f:
    n = int(f.readline())
    s1,s2,s3 = eval(f.readline()),eval(f.readline()),{i for i in range(1,n+1)}
    print(s1 | s2)
    print(s1 & s2)
    print(s1 - s2)
    print(s2 - s1)
    print(s3 - s1)
    print(s3 - s2)