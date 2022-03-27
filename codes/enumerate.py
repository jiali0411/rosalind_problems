from itertools import product
from itertools import permutations
def orders(n):
    element_list = []
    for i in range(1,n+1):
        element_list.append([-i,i])
    all_possible = permutations(element_list)
    for possible in all_possible:
        print list(product(*possible))

    return None

if __name__ == "__main__":
    n = 3
    orders(n)