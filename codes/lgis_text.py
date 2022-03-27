def readFile(fileName):
    with open(fileName) as f:
        n = f.readline().strip("\n")
        seq = f.readline().strip("\n")
    return int(n), seq

def longest_increasing_sub(n, seq, increasing = True):
    l =[]
    for i in range(n):
        number = int(seq[i])
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

            max_temp = max(temp, key=len)
            l.append(max_temp + [number])
    return max(l,key=len)

def print_list_to_number(a_list):
    for number in a_list:
        print(number, end= " ")

def main():
    import sys
    input_file = sys.argv[1]
    n , seq = readFile(input_file)
    d = seq.split(" ")
    max_increase = longest_increasing_sub(n, d, increasing=True)
    max_decrease = longest_increasing_sub(n,d, increasing=False)
    print_list_to_number(max_increase)
    print()
    print_list_to_number(max_decrease)
main()