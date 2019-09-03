"""
Created on Sep 1st, 2019
Author: Jiali
This is the solution for rosalind question 'Longest Increasing Subsequence'
"""
# Give an integer n, followed by a permutation of length n. 

def permutation(seq, reverse):
    results = []
# If seq is empty, the permutation is an empty list
    if len(seq) == 0:
        return []
# If there is only one element in lst then, only one permuatation is possible 
    if len(seq) == 1:
        results.append(seq)
        return results

    remain = seq[:-1]
    remain_list = permutation(remain, reverse)

    for item in remain_list:
        new_item = item[:]
        if not reverse:
            if int(new_item[-1]) < int(seq[-1]):
                new_item.append(seq[-1])
                results.append(new_item)
            results.append(item)
        else:
            if int(new_item[-1]) > int(seq[-1]):
                new_item.append(seq[-1])
                results.append(new_item)
            results.append(item)

    results.append([seq[-1]])
    return results

def Longest(results):
    max_seq = max(results,key=len)
    max_sub = ""
    for i in max_seq:
        max_sub = max_sub+str(i)+" "
    return max_sub

def main():
    with open("/Users/jiali/Desktop/Jiali/UTK/2019 Fall/rosalind_problems/datasets/rosalind_lgis.txt") as input_file:
        content = input_file.readlines()
        n = content[0].strip("\n")
        seq = content[1].strip("\n").split(" ")
        res = permutation(seq, reverse = False)
        max_inc = Longest(res)
#    new_res = permutation(seq, reverse = True)
#    max_dec = Longest(new_res)
        print max_inc
#    print max_dec
main()

"""
 Reference: the permutaion function is followed 
 with method 3 in https://www.geeksforgeeks.org/generate-all-the-permutation-of-a-list-in-python/
"""