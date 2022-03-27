"""
Created on Nov 6th
Author: Jiali
This is the solution for rosalind problem "counting point mutation"
"""

import sys

def readfile(filename):
    input_seq =[]
    with open(filename) as f:
        for line in f:
            seq = line.strip('\n')
            input_seq.append(seq)
    return input_seq

def hamming_distance(s1, s2):
    n = len(s1)
    d = 0
    for i in range(n):
        if s1[i] == s2[i]:
            continue
        else:
            d = d +1
    print d
    return None

if __name__ == "__main__":
    my_file = sys.argv[1]
    my_seq = readfile(my_file)
    hamming_distance(my_seq[0], my_seq[1])
