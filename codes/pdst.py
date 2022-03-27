"""
Nov 12, 2019
Author: Jiali
This is the solution for rosalind problem 'Creating a Distance Matrix'
"""

import sys

def readFastaFile(fileName):
    with open(fileName) as f:
        seq= ""
        for line in f:
            if line.startswith(">"):
                seq= seq+"\n"
            else:
                seq = seq+line.strip("\n")
    seq_list = seq.split("\n")

    return seq_list

def calculate_distance(seq1, seq2):
    size = len(seq1)
    d = 0
    for i in range(size):
        if seq1[i] != seq2[i]:
            d = d +1
    return float(d)/float(size)

# def distance_matrix(seq_list):
#     for i in seq_list:
#         for every_seq in seq_list:
#             p_distance = calculate_distance(i, every_seq)
#             print '%.4f' % p_distance,
#         print    
#     return None

# if __name__ == "__main__":
#     file_input = sys.argv[1]
#     sequences = readFastaFile(file_input)
#     distance_matrix(sequences[1:])