with open('./testcase/rosalind_tree.txt', 'r') as f:
   print(int(f.readline())-len(f.readlines())-1)
