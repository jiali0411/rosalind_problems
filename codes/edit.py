"""
Created on Sep 5, 2019
Author: Jial
This is the solution for rosalind problem 'edit distance'
Referece: An introudction to bioinformatics algorithms Chapter 6.5 Page 176-177
"""
import argparse
import numpy as np

parser = argparse.ArgumentParser(description="compute edit distance", usage="%(prog)s -i input_file ")
parser.add_argument("-i", type=str, help="input file")
args = parser.parse_args()
file_in = args.i

def editDistance(s,t):
    # find the minimun edit distance of s and t, algorithm refered from the book. 
    n = len(s) + 1
    m = len(t) + 1
    array = np.zeros((n,m), dtype=int)
    array[:,0] = np.arange(n)
    array[0,:] = np.arange(m)

    for i in range(1,n):
        for j in range(1,m): 
            if s[i-1] == t[j-1]:
                array[i,j] = array[i-1,j-1]
            else:
                array[i,j] = min(array[i-1,j]+1, array[i,j-1]+1, array[i-1,j-1]+1)

    edits = array[-1][-1]
    print edits
    return None

def readFastaFile(fileName):
    with open(fileName) as f:
        s= ""
        n=0
        for line in f:
            if line.startswith(">"):
                s= s+"\n"
            else:
                s = s+line.strip("\n")
    return s

if __name__ == "__main__":
    sequences = readFastaFile(file_in)
    s = sequences.split("\n")
    edit = editDistance(s[1],s[2])