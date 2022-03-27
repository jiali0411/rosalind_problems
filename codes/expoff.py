"""
Created on Nov 6
Author: Jiali
This is the solution for rosaline problem 'Calculating expected offspring'
"""
import sys

def readfile(fileName):
    with open(fileName) as f:
        content = f.readline()
        inputs = content.split(" ")
    integers = []
    for i in inputs:
        number = int(i)
        integers.append(number)
    return integers

def expected_offspring(integers):
    Dominant1 = integers[0] * 2
    Dominant2 = integers[1] * 2
    Dominant3 = integers[2] * 2
    Dominant4 = integers[3] * 2 * 0.75
    Dominant5 = integers[4] * 2 * 0.5
    return Dominant1 + Dominant2 + Dominant3 + Dominant4 + Dominant5

if __name__ == "__main__":
    input_file = sys.argv[1]
    input_integers = readfile(input_file)
    expect = expected_offspring(input_integers)
    print expect
