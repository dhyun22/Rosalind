with open('./data/rosalind_revc.txt','r') as file:
    DNA = file.read()

def complement(DNA):
    seq=''
    DNA_list=list(DNA)
    DNA_list.reverse()
    for i in DNA_list:
        if i=='A':
            seq+='T'
        if i=='T':
            seq+='A'
        if i=='G':
            seq+='C'
        if i=='C':
            seq+='G'
    print(seq)

complement(DNA)