"""
Created on Sep 9th, 2019
Author: Jiali
This is the solution for rosalind problem 'Find a Longest Common Subsequence of Two Strings'
Reference: An introduction to bioinformatics algorithms Chaptor 6.5 and
            https://www.geeksforgeeks.org/python-program-for-longest-common-subsequence/
"""
import argparse
parser = argparse.ArgumentParser(description="compute edit distance", usage="%(prog)s -i input_file ")
parser.add_argument("-i", type=str, help="input file")
args = parser.parse_args()
file_in = args.i

def longestCommon(a, b):
    n = len(a) +1
    m = len(b) +1
    score = [[0]* m for i in range(n)]
    com_list = [[None]* m for i in range(n)]
    for i in range(1,n):
        for j in range(1,m):
            if a[i-1] == b[j-1]:
                score[i][j] = score[i-1][j-1]+1
                com_list[i][j] = "cross"
            else:
                score[i][j] = max(score[i-1][j],score[i][j-1])
                if score[i][j] == score[i-1][j]:
                    com_list[i][j] = "up"
                elif score[i][j] == score[i][j-1]:
                    com_list[i][j] = "left"
        # print score[i].index(min(score[i][1:]))
    return com_list

def printLCS(com_list,a,i,j):
    s = ""
    while i  > 0:
        while j > 0:
            if com_list[i][j] == "cross":
                s = s + a[i-1]
                i = i -1
                j = j -1
            else:
                if com_list[i][j] == "up":
                    i = i - 1
                    j = j
                else:
                    i = i
                    j = j - 1

    return s[::-1]

def readFile(fileName):
    with open(fileName) as f:
        s = f.readlines()
    return s


if __name__ == "__main__":
    seq = readFile(file_in)
    s1 = seq[0].strip("\n")
    s2 = seq[1].strip("\n")
    common_seq = longestCommon(s1,s2)
    print printLCS(common_seq, s1, len(s1), len(s2))