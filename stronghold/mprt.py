import re
import requests
with open('./testcase/rosalind_mprt.txt','r') as f:
    motif=re.compile('(?=N[^P][ST][^P])')
    for uniprot_id in f.readlines():
        query=uniprot_id.strip().split('_')[0]
        url=f'https://rest.uniprot.org/uniprotkb/search?query={query}&format=fasta'
        fasta = ''.join(requests.get(url).text.split('\n')[1:])
        matches = [match.start()+1 for match in motif.finditer(fasta)]
        if not matches: continue
        print(uniprot_id,end='')
        for i in matches: print(i,end=' ')
        print()
