from Bio import Entrez,SeqIO
Entrez.email = 'your_name@your_mail_server.com' # Sorry...
with open('./testcase/rosalind_frmt.txt','r') as f:
    ids = f.readline().strip().split()
    records = list(SeqIO.parse(Entrez.efetch(db='nucleotide',id=ids,rettype='fasta'),'fasta'))
    min_len,r = int(1e9),None
    for entry in records:
        if len(entry.seq) < min_len:
            min_len,r = len(entry.seq),entry
    SeqIO.write(r,handle='out.txt',format='fasta')