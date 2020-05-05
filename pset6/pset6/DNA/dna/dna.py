from csv import reader, DictReader
from sys import argv

if len(argv) != 3:
    print("usage error, dna.py sequence.txt database.csv")
    exit(1)

with open(argv[2]) as DNAfile:
    DNAreader = reader(DNAfile)
    for row in DNAreader:
        DNAlist = row

DNA = DNAlist[0]
sequences = {}

with open(argv[1]) as tablefile:
    table = reader(tablefile)
    for row in table:
        DNASequence = row
        DNASequence.pop(0)
        break

for item in DNASequence:
    sequences[item] = 1

for key in sequences:
    l = len(key)
    tempMax = 0
    temp = 0
    for i in range(len(DNA)):
        while temp > 0:
            temp -= 1
            continue

        if DNA[i: i + l] == key:
            while DNA[i - l: i] == DNA[i: i + l]:
                temp += 1
                i += l

            if temp > tempMax:
                tempMax = temp

    sequences[key] += tempMax

with open(argv[1]) as file:
    matching = DictReader(file)
    for person in matching:
        match = 0
        for dna in sequences:
            if sequences[dna] == int(person[dna]):
                match += 1
        if match == len(sequences):
            print(person["name"])
            exit(0)

    print("No match")