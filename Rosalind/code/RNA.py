def transcription(t):
    RNA = ''
    for i in t:
        if i == 'T':
            RNA += 'U'
        else:
            RNA += i
    return RNA

with open('./data/rosalind_rna.txt','r') as file:
    DNA = file.read()

print(transcription(DNA))