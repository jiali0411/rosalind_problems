"""
Created on Sep 12, 2019
Author: Jiali
This is the solution for rosalind problem 'Edit Distance Alignment'
"""
import argparse
import numpy as np

parser = argparse.ArgumentParser(description="compute edit distance alignment", usage="%(prog)s -i input_file ")
parser.add_argument("-i", type=str, help="input file")
args = parser.parse_args()
file_in = args.i

def editAlign(s, t):
    # First, find the edit distance from the script 
    n = len(s) + 1
    m = len(t) + 1
    array = np.zeros((n,m), dtype=int)
    array[:,0] = np.arange(n)
    array[0,:] = np.arange(m)
    edits = [[None]* m for i in range(n)]
    for i in range(1,n):
        for j in range(1,m): 
            if s[i-1] == t[j-1]:
                array[i,j] = array[i-1,j-1]
                edits[i][j] = "cross"
            else:
                array[i,j] = min(array[i-1,j]+1, array[i,j-1]+1, array[i-1,j-1]+1)
                if array[i,j] == array[i-1,j]+1:
                    edits[i][j] = "up"
                elif array[i,j] == array[i,j-1]+1:
                    edits[i][j] = "left"
                else:
                    edits[i][j] = "exchange"
    print array[n-1,m-1]
    return edits

def printalignment(edits, s, t):
    seq1 = ""
    seq2 = ""
    i = len(s)
    j = len(t)
    while i > 0:
        while j > 0:
            print i, j
            if edits[i][j] == "cross":
                seq1 = seq1+s[i-1]
                seq2 = seq2+t[j-1]
                i = i-1
                j = j-1
            elif edits[i][j] == "up":
                seq1 = seq1 + s[i-1]
                seq2 = seq2 + "-"
                i = i-1
                j = j
            elif edits[i][j] == "left":
                seq1 = seq1 + "-"
                seq2 = seq2 + t[j-1]
                i = i
                j = j-1
            else:
                seq1 = seq1 + s[i-1]
                seq2 = seq2 + t[j-1]
                i = i-1
                j = j-1
    print seq1[::-1]
    print seq2[::-1]
    return None

def openFasta(fileName):
    s = ""
    with open(fileName) as f:
        for line in f:
            if line.startswith(">"):
                s = s + "\n"
            else:
                s = s + line.strip("\n")
    seq = s.split("\n")
    return seq

if __name__ == "__main__":
    s = openFasta(file_in)
    alignment = editAlign(s[1],s[2])
    printalignment(alignment, s[1], s[2])
