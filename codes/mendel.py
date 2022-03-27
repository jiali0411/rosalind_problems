"""
Created on Sep 25, 2019
Author: Jiali
This is the solution for rosalind problem 'Mendel's first law'
"""
import math

k = 27
m = 21
n = 27
# Calculate fatorial number
def nCr(p,r):
    f = math.factorial
    return float(f(p) / (f(r) * f(p-r)))

def Prob_dominant(k,m,n):
    total = k+m+n
    # Calculate the ressessive probability, then the dominant probability is 1 - ressessive probablity
    # 1. when selecting from the ressesive population n, the propability is:
    n_prob = nCr(n,2)/nCr(total,2)
    # 2. When selecting from the heterozygous population n, the probability is:
    m_prob = nCr(m,2)/nCr(total,2) * 1./4.
    # 3. When selecting one from heterizygous and one from ressesive, the probability is:
    nm_prob = (n*m)/nCr(total,2) * 1./2.
    # dominant probability is 1 - all ressessive probability
    dominant = 1 - n_prob - m_prob - nm_prob
    return dominant

if __name__ == '__main__':
    print Prob_dominant(k,m,n)