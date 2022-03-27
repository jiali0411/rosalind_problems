"""
Aug 28, 2019
Author: Jiali
This program is the solution for rosalind problem 'Rabbits and Recurrence Relations'
"""
# Calculate the fibonacci sequence
# First compute when k = 1, get the right for loop
# Then compute recurrence with k
def recurrence(n, k):
    F_1 = 0
    F_2 = 1
    S = 0 
    for i in range(n-1):
        S = F_1 + F_2
        F_1 = F_2 * k 
        F_2 = S
    return S

def main():
    n = 35
    k = 5
    print recurrence(n, k)
main()