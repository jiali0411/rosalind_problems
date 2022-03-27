"""
2020.May.06
Author: Jiali
This is the solution for rosalind problem complementing a strand of DNA
"""

import argparse

parser = argparse.ArgumentParser(description="complementing a strand of DNA", usage="%(prog)s -i input_file ")
parser.add_argument("-i", type=str, help="input file")
args = parser.parse_args()
file_in = args.i

with open(file_in) as f:
    seq = f.read()
    comp_seq = seq.replace("A","t").replace("T","a").replace("C","g").replace("G","c")
    revc_seq = comp_seq.upper()[::-1]
    print(revc_seq)

