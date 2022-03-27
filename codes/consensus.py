import sys
from pdst import readFastaFile

file_in = sys.argv[1]

def find_consensus(seq_list, length):
    A = []
    C = []
    G = []
    T = []
    for i in range(length):
        position = ""
        for seq in seq_list:
            position = position + seq[i]
        A.append(position.count("A"))
        C.append(position.count("C"))
        G.append(position.count("G"))
        T.append(position.count("T"))
    string = "ACGT"
    
    for i in range(length):
        s = [A[i],C[i],G[i],T[i]]
        idx = s.index(max(s))
        print(string[idx], end="")
    print()
    print("A:", " ".join(map(str,A)))
    print("C:", " ".join(map(str,C)))
    print("G:", " ".join(map(str,G)))
    print("T:", " ".join(map(str,T)))
    return None

if __name__ == "__main__":
    seq_list = readFastaFile(file_in)
    seq_length = len(seq_list[1])
    find_consensus(seq_list[1:], seq_length)