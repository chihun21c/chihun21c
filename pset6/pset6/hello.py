import csv
from sys import argv, exit


#딕셔너리 만들기
dictionary = {}


#csv파일 읽기
with open("small.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        name = row[0]
        DNA = tuple(row[1:])
        dictionary.update = {name,DNA}
print(dictionary)