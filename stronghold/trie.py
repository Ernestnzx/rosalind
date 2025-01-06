class Node:
    def __init__(self, c, idx):
        self.alphabet = c
        self.child = [None for _ in range(4)]
        self.idx = idx

class Trie:
    def __init__(self):
        self.root = Node('#',1)
        self.size = 1

    def insert(self, word):
        curr = self.root
        for c in word:
            idx = 'ACGT'.find(c)
            if not curr.child[idx]:
                curr.child[idx] = Node(c,self.size+1)
                self.size += 1
            curr = curr.child[idx]
    
    def traverse(self, u=None):
        if not u: 
            u = self.root;
        for v in u.child:
            if not v: continue
            print(u.idx,v.idx,v.alphabet)
            self.traverse(v)
        
trie = Trie()
with open('./testcase/rosalind_trie.txt','r') as f:
    for dna in f.readlines():
        trie.insert(dna.strip())
trie.traverse()
