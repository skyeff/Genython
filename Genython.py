class gen:
    def __init__(self, file):
        self.file = file

    def seq(self):
        with open(self.file, 'r') as file:
            next(file)  # Descarta primeira linha
            content = file.read()
        return content.replace('\n', '').replace(' ', '')

    def __str__(self): return self.seq()

    def getbases(self):
        counts = {'A':0, 'C':0, 'T':0, 'G':0}
        for base in self.seq(): 
            if base in counts: counts[base] += 1
        return counts
        

    def complement(self):
        complement_map = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
        return "".join([complement_map[base] for base in self.seq() if base in complement_map])

    def transcribe(self):
        return "".join(map(lambda base: 'U' if base == 'T' else base, self.seq())) 


    def reverse(self): return self.seq()[::-1]

    def translate(self):
        genetic_code = {
            # Fenilalanina (F)
            'UUU': 'F', 'UUC': 'F',
            # Leucina (L)
            'UUA': 'L', 'UUG': 'L', 'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',
            # Serina (S)
            'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S', 'AGU': 'S', 'AGC': 'S',
            # Tirosina (Y)
            'UAU': 'Y', 'UAC': 'Y',
            # Stop codons (códons de terminação)
            'UAA': '*', 'UAG': '*', 'UGA': '*',
            # Cisteína (C)
            'UGU': 'C', 'UGC': 'C',
            # Triptofano (W)
            'UGG': 'W',
            # Prolina (P)
            'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
            # Histidina (H)
            'CAU': 'H', 'CAC': 'H',
            # Glutamina (Q)
            'CAA': 'Q', 'CAG': 'Q',
            # Arginina (R)
            'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R', 'AGA': 'R', 'AGG': 'R',
            # Isoleucina (I)
            'AUU': 'I', 'AUC': 'I', 'AUA': 'I',
            # Metionina (M) - também start codon
            'AUG': 'M',
            # Treonina (T)
            'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
            # Asparagina (N)
            'AAU': 'N', 'AAC': 'N',
            # Lisina (K)
            'AAA': 'K', 'AAG': 'K',
            # Valina (V)
            'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',
            # Alanina (A)
            'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
            # Ácido aspártico (D)
            'GAU': 'D', 'GAC': 'D',
            # Ácido glutâmico (E)
            'GAA': 'E', 'GAG': 'E',
            # Glicina (G)
            'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'
            }
        sequence = self.transcribe()
        bases = [sequence[base:base+3] for base in range(0, len(sequence), 3)]
        aminoacids = ""
        for codon in bases:
            if codon in genetic_code: aminoacids += genetic_code[codon]
            else: aminoacids += 'X'
        return aminoacids

genome = gen("MycGen.fasta")
print(genome.translate())
