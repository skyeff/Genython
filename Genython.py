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
        complement = ""
        complement_map = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
        for base in self.seq():
            if base in complement_map: complement +=  complement_map[base]
            else  : complement += base
        return complement

    def transcribe(self):
        transcript = "" 
        for base in self.seq():
            if base == 'T': transcipt += 'U'
            else : transcript += base

    def reverse(self): return self.seq()[::-1]

