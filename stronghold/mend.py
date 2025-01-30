with open('./testcase/rosalind_mend.txt','r') as f1:
    pb = {
        ("AA", "AA"): (1.0, 0.0, 0.0),
        ("AA", "Aa"): (0.5, 0.5, 0.0),    
        ("AA", "aa"): (0.0, 1.0, 0.0),
        ("Aa", "AA"): (0.5, 0.5, 0.0), 
        ("Aa", "Aa"): (0.25, 0.5, 0.25),
        ("Aa", "aa"): (0.0, 0.5, 0.5),
        ("aa", "AA"): (0.0, 1.0, 0.0),
        ("aa", "Aa"): (0.0, 0.5, 0.5),
        ("aa", "aa"): (0.0, 0.0, 1.0)
    }
    def f(s,t):
        p = {"AA":0.0, "Aa":0.0, "aa":0.0}
        for k1,v1 in s.items():
            for k2,v2 in t.items():
                p["AA"] += v1*v2*pb[(k1,k2)][0]
                p["Aa"] += v1*v2*pb[(k1,k2)][1]
                p["aa"] += v1*v2*pb[(k1,k2)][2]
        return p
    # Base case of the recursion
    AA = {"AA":1.0, "Aa":0.0, "aa":0.0}
    Aa = {"AA":0.0, "Aa":1.0, "aa":0.0}
    aa = {"AA":0.0, "Aa":0.0, "aa":1.0}
    print(*eval(f1.readline().replace('(','f(').replace(';','')).values())
    