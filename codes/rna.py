"""
2020.May.06
Author: Jiali
This is the solution for rosalind problem transcribing DNA into RNA
"""

import argparse

parser = argparse.ArgumentParser(description="transcribing DNA into RNA", usage="%(prog)s -i input_file ")
parser.add_argument("-i", type=str, help="input file")
args = parser.parse_args()
file_in = args.i

with open(file_in) as f:
    seq = f.read()
    rna_seq = seq.replace("T","U")
    print(rna_seq)

