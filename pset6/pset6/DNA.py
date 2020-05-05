import csv
from sys import argv, exist

#커멘드 입력의 실수가 있을경우:
if len(argv) != 3:  
    print("Usage: python dna.py data.csv sequence.txt")
exit(1)

#딕셔너리 만들기
dictionary = {}

#csv파일 읽어 드리기
with open(argv[1]) as csvfile:
    read = csv.reader(csvfile)
    for STR in read:
        DNAtype = tuple(STR[1:])
    break
    next(csvfile)
    for row in read:
        name = row[0]
        DNA = tuple(row[1:])
        dictionary1 = {name:DNA}
        dictionary.update(dictionary1)
    break    


text = open(argv[2], "r").read()    
for i in range(len(DNA)):
    Sample = DNAtype[i]
    L_sample = len(Sample)
    
    string = text 
    
    r1 = re.finall(r"(({})+)".format(Sample),string)

    matches = [ x[0] for x in r1]

    for match in matches:
        repetition = int(len(match/L_sample)
    print(dna_type[i])
    print(repetition)
    
#프린트 하기 

