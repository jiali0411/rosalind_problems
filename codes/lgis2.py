def increasing_subsequence(d, n):
    'Return one of the L.I.S. of list d'
    l = []
    for i in range(n):
        # This is a slow algorithm
        # if l == []:
        #     l.append([int(d[i])])
        # else:
        #     l.append([int(d[i])])
        #     for j in xrange(len(l)):
        #         if l[j][-1] < int(d[i]):
        #             l.append(l[j] + [d[i]])
        # print l
# a faster algorithm refer to 'https://rosettacode.org/wiki/Longest_increasing_subsequence#Python:_Method_from_video'
# loop over each item in the sequence and add the element into the longest subsequence if condition matched.
        #l.append(max([l[j] for j in range(i) if l[j][-1] < int(d[i])] or [[]], key=len) + [int(d[i])])
        # When l is empty, add d[i]
        if l == []:
            l.append([int(d[i])])
        # if l has at least one element, start counting the max length of the element match the condition (increasing: the last number in the element is smaller than d[i])
        else:
            # create an empty list as current list
            curr = []
            # for each element before i, compare the last item in the element with d[i]
            # if match the condition, append the element into current list, otherwise append an empty list
            for j in range(i):
                if l[j][-1] < int(d[i]):
                    curr.append(l[j])
                else:
                    curr.append([])
            # find the longest element in current list
            max_sub = max(curr,key=len)
        # only add d[i] into the longest element of current list and append the new list into l.
            l.append(max_sub + [int(d[i])])          
    # Then return the longest element in l, which will output the first longest, not all the longest subsequences. 
    return max(l, key=len)
 
def main():
    # d= [8, 2, 1, 6, 5, 7, 4, 3, 9]
    # print increasing_subsequence(d, 9)
    # d = [5,1,4,2,3]
    # print increasing_subsequence(d,5)
    with open("/Users/jiali/Desktop/Jiali/UTK/2019 Fall/rosalind_problems/datasets/rosalind_lgis.txt") as input_file:
        content = input_file.readlines()
        n = int(content[0].strip("\n"))
        seq = content[1].strip('\n').split(' ')
        #d = [int(i) for i in seq]
        print increasing_subsequence(seq, n)

main()