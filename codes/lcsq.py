"""
Created on Sep 5th, 2019
Author: Jiali
This is the solution for rosalind problem 'finding a spliced motif'
"""
import argparse
parser = argparse.ArgumentParser(description="finding the index of a shared motif", usage="%(prog)s -i input_file ")
parser.add_argument("-i", type=str, help="input file")
args = parser.parse_args()
file_in = args.i

def findMotif(s, t):
    j = 0
    for i,letter in enumerate(s):
        # print i, letter
        if letter == t[j]:
            print i+1,
            j = j+1
            if j >= len(t):
                break
    return None

if __name__ == "__main__":
    with open(file_in) as f:
        s = ""
        n = 0
        for line in f:
            if line.startswith(">"):
                header = line.strip(">")
                n = n+1
                if n == 2:
                    t = f.next()
            else:
                seq = line.strip("\n")
                s = s + seq
        idx = findMotif(s, t)


                