def increasing_subsequence(d, n):
    'Return one of the L.I.S. of list d'
    l = []
    for i in range(n):
        # This is a slow algorithm
        l.append([d[i]])
        for j in range(len(l)):
            if l[j][-1] < d[i]:
                l.append(l[j] + [d[i]])
        print l
# a faster algorithm refer to 'https://rosettacode.org/wiki/Longest_increasing_subsequence#Python:_Method_from_video'
# loop over each item in the sequence and add the element into the longest subsequence if condition matched.
        #l.append(max([l[j] for j in range(i) if l[j][-1] < int(d[i])] or [[]], key=len) + [int(d[i])])
        # When l is empty, add d[i]
    #     if l == []:
    #         l.append([int(d[i])])
    #     # if l has at least one element, start counting the max length of the element match the condition (increasing: the last number in the element is smaller than d[i])
    #     else:
    #         max_len = 0
    #         for j in range(len(l)):
    #             if l[j][-1] < int(d[i]):
    #                 max_len = max(max_len, len(l[j]))
    #     # if no element match the condition, the max_len should still be 0, then add this d[i] into l.
    #         if max_len == 0:
    #             l.append([int(d[i])])
    #     # Then loop over the l again, and add the d[i] to the element match the condition (last number is smaller than d[i] and the element is the longest)
    #         for j in range(len(l)):
    #             if l[j][-1] < int(d[i]) and len(l[j]) == max_len:
    #                 l.append(l[j]+[int(d[i])])  
    # # Then return the longest element in l, which will output the first longest, not all the longest subsequences. 
    return max(l,key=len)
 
def main():
    # d= [8, 2, 1, 6, 5, 7, 4, 3, 9]
    # print increasing_subsequence(d, 9)
    d = [5,1,4,2,3]
    print increasing_subsequence(d,5)
    # with open("/Users/jiali/Desktop/Jiali/UTK/2019 Fall/rosalind_problems/datasets/rosalind_lgis.txt") as input_file:
    #     content = input_file.readlines()
    #     n = int(content[0].strip("\n"))
    #     seq = content[1].strip('\n').split(' ')
    #     #d = [int(i) for i in seq]
    #     print increasing_subsequence(seq, n)
main()