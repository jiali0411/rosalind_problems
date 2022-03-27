"""
Created on Sep 17, 2019
Author: Jiali
This is the solution for rosalind proble 'Global alignment with scoring matrix'
Referece: Introduction to Bioinformatics Algorithms Chapter 6.6 Global Sequence Alignment Page 177-178
"""

import argparse
import numpy as np
import pandas as pd

parser = argparse.ArgumentParser(description="global alignment scoring", usage="%(prog)s -i fasta_file -m matrix_file ")
parser.add_argument("-i", type=str, help="input fasta file")
parser.add_argument("-m", type=str, help="matrix file")
args = parser.parse_args()
file_in = args.i
file_mat = args.m

def readMatrix(fileName):
    matrix = pd.read_table(fileName, index_col =0, sep = "\s+")
    return matrix

def score(matrix,x,y):
    my_score = matrix.at[x,y]
    return int(my_score)

def alignScore(s,t, matrix):
    n = len(s) + 1
    m = len(t) + 1
    array = np.zeros((n,m), dtype=int)
    array[:,0] = np.arange(n) * -5
    array[0,:] = np.arange(m) * -5
    for i in range(1,n):
        for j in range(1,m): 
            temp1 = array[i-1,j-1] + score(matrix, s[i-1], t[j-1])
            temp2 = array[i,j-1] - 5
            temp3 = array[i-1,j] - 5
            array[i,j] = max(temp1, temp2, temp3)
                    
    print array[n-1,m-1]
    return None

def readFasta(fileName):
    with open(fileName) as f:
        seq= ""
        n=0
        for line in f:
            if line.startswith(">"):
                seq= seq+"\n"
            else:
                seq = seq+line.strip("\n")
    return seq



if __name__ == "__main__":
    matrix = readMatrix(file_mat)
    fastaSeq = readFasta(file_in)
    s = fastaSeq.split("\n")
    edit_matrix = alignScore(s[1], s[2], matrix)