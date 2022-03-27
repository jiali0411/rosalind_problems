"""
2020.May.06
Author: Jiali
This is the solution for rosalind problem counting DNA nucleotides
"""

import argparse

parser = argparse.ArgumentParser(description="counting DNA nucleotides", usage="%(prog)s -i input_file ")
parser.add_argument("-i", type=str, help="input file")
args = parser.parse_args()
file_in = args.i

with open(file_in) as f:
    seq = f.read()
    print(seq)
    A_nub = seq.count("A")
    C_nub = seq.count("C")
    G_nub = seq.count("G")
    T_nub = seq.count("T")
    print(A_nub, C_nub, G_nub, T_nub)

