## rewrite the lgis codes
## give a sequence of numbers d, and the length n, return the longest increasing subsequence.

import sys
def readFile(fileName):
    with open(fileName) as f:
        n = f.readline().strip("\n")
        d = f.readline().strip("\n").split(" ")
    return int(n), d

def longest_increase_sub(n,d,increasing = True):
    l = []
    for i in range(n):
        number = int(d[i])
        if l == []:
            l.append([number])
        else:
            temp = []
            for j in range(i):
                if increasing:
                    if l[j][-1] < number:
                        temp.append(l[j])
                    else:
                        temp.append([])
                elif increasing == False:
                    if l[j][-1] > number:
                        temp.append(l[j])
                    else:
                        temp.append([])
            max_sub = max(temp,key=len)
            l.append(max_sub + [number])
            #print(l)          
    return max(l, key=len)

def print_list_to_number(a_list):
    for number in a_list:
        print(number, end=" ")
    return None

def main():
    input_file = sys.argv[1]
    n, d = readFile(input_file)
    max_increase = longest_increase_sub(n,d)
    max_decrease = longest_increase_sub(n,d,increasing=False)
    print_list_to_number(max_increase)
    print()
    print_list_to_number(max_decrease)
    print()
main()

