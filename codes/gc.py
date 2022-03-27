"""
Created on May 08, 2020
Author: Jiali
This is the solution for rosalind proble 'computing GC content'
"""

import argparse

parser = argparse.ArgumentParser(description="computing GC content", usage="%(prog)s -i fasta_file ")
parser.add_argument("-i", type=str, help="input fasta file")
args = parser.parse_args()
file_in = args.i

def readFasta(fileName):
    with open(fileName) as f:
        seq= ""
        names = []
        for line in f:
            if line.startswith(">"):
                names.append(line.strip(">"))
                seq= seq+"\n"
            else:
                seq = seq+line.strip("\n")
    return names, seq

def gc_content(seq):
    G_pct = seq.count("G")/len(seq) * 100
    C_pct = seq.count("C")/len(seq) * 100
    return G_pct+C_pct

if __name__ == "__main__":
    headers, fastaSeq = readFasta(file_in)
    s = fastaSeq.split("\n")
    gc_list = []
    for seq in s[1:]:
        gc_pct = gc_content(seq)
        gc_list.append(gc_pct)
    max_gc = max(gc_list)
    idx = gc_list.index(max_gc)
    print(headers[idx]+str(max_gc))
