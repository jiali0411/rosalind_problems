"""
Create on Aug28, 2019
Author: Jiali
This is solution for rosalind problem 'Mortal Fibonacci Rabbits'
"""

# Store fibonacci sequence into a list so it can be tracked
def reccurrence(n, m):
    F1 = 0
    F2 = 1
    S = 0
    sequence = [1,1]
    for i in range(1,n):
        if i < m:
            S = F1 + F2
            sequence.append(S)
            F1 = F2
            F2 = S
        else:
            die = sequence[i-m]
            S = F1 + F2 - die
            sequence.append(S)
            F1 = F2
            F2 = S
    return S

def main():
    n = 81
    m = 16
    print reccurrence(n,m)
main()