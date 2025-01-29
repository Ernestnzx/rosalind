from Bio import Entrez
with open('./testcase/rosalind_gbk.txt','r') as f:
    o = f.readline().strip()
    d1 = f.readline().strip()
    d2 = f.readline().strip()
    query = f'"{o}"[Organism] AND ("{d1}"[PDAT] : "{d2}"[PDAT])'
    Entrez.email = 'your_name@your_mail_server.com' # Sorry...
    print(Entrez.read(Entrez.esearch(db='nucleotide',term=query))['Count'])