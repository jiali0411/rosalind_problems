"""
Created on Oct 1
Author: Jiali
This is the solution for rosalind problem 'Global Alignment with Constant Gap Penalty'
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

# import three functions from file glob.py
from glob import readFasta, readMatrix, score

def CalculateScore_Penalty(s, t, matrix):
    n = len(s) + 1
    m = len(t) + 1
    array = np.zeros((n,m), dtype=int)
    array[:,0] = np.arange(n) * -5
    array[0,:] = np.arange(m) * -5
    for i in range(1,n):
        for j in range(1,m):
            


    return None

if __name__ == "__main__":
    fastaSeq = readFasta(file_in)
    matrix = readMatrix(file_mat)
    s = fastaSeq.split("\n")


