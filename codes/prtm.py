"""
Created on Oct 28
Author: Jiali
This is the solution for rosalind problem calculating protein mass
"""
import sys

def import_MassTable(table_file):
    mass = {}
    with open(table_file) as f:
        for line in f:
            line_list = line.strip("\n").split("   ")
            mass[line_list[0]] = float(line_list[1])
    return mass

def calculate_ProteinMass(input_file, mass):
    with open(input_file) as f:
        seq = f.readline().strip('\n')
    weight = 0
    for aa in seq:
        weight = weight + mass[aa]
    print weight

if __name__ == "__main__":
    mass_table = sys.argv[1]
    mass = import_MassTable(mass_table)
    protein = sys.argv[2]
    calculate_ProteinMass(protein, mass)
