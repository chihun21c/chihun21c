import csv
from sys import argv, exit

#커멘드 입력의 실수가 있을경우:
if len(argv) != 3:  
    print("Usage: python dna.py data.csv sequence.txt")
exit(1)

#딕셔너리 만들기
dictionary = {}
DNAdictionary = {}

#csv파일 읽기
with open(argv[1]) as csvfile:
    csvreader = csv.DictReader(csvfile)
    for row in csvreader:
        name = row[0]
        DNA = tuple(row[1:])
        dictionary.update = {name,DNA}
    

#txt 파일 읽기
with open(argv[2]) as textfile:
    txtreader = csv.reader(textfile)
    if re.search("^AGATC?$", txtreader):
        
    


    next(csvfile)
    for row in read:
        name = row[0]
        DNA = tuple(row[1:])
        dictionary1 = {name:DNA}
        dictionary.update(dictionary1)
       

with open(argv[2]) as textfile:
    text = csv.reader(textfile)
    for DNAsequence in text:
        Sample = tuple(DNAsequence)
        a = Sample.count('AGAT')
        b = Sample.count('AATG')
        c = Sample.count('TATC')


    print(f"{name.dictionary1}")
    print(f"{a}")
    print(f"{b}")
    print(f"{c}")