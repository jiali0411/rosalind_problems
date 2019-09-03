def longest_sub(l):
    result =[]
    for num, i in enumerate(l):
        i = int(i)
        curr = [int(num)]
        j = i+1
        while j < len(l):
            a = int(l[j])
            if a > curr[len(curr)-1]:
                curr.append(a)
            j = j+1
        if len(result) < len(curr):
            result = curr[:]
    return result

if __name__ == "__main__":
    with open("/Users/jiali/Desktop/Jiali/UTK/2019 Fall/rosalind_problems/datasets/rosalind_lgis.txt") as input_file:
        content = input_file.readlines()
        n = int(content[0].strip("\n"))
        seq = content[1].strip('\n').split(' ')
        # d = [int(i) for i in seq]
        print longest_sub(seq)    