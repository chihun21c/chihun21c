import csv
import sys
import copy

dbPath = sys.argv[1]
seqPath = sys.argv[2]

if len(sys.argv) > 3:
    print("error")
    exit()

str_list = []
DB = open(dbPath, 'r')
DBreader = csv.DictReader(DB)
for row in DBreader:
    #    print(DBreader.fieldnames)
    # Store the str for checking in SEQ
    str_list = DBreader.fieldnames
#Remove "Name" field from list
str_list.pop(0)

seq_dict ={}
seq_dict = dict.fromkeys(str_list,1)
#print(seq_dict)

cur_count = 1
SQ = open(seqPath, "r")
for line in SQ:
    for y in range(len(str_list)):
        for i in range(len(line)):
            #Check for condition of matching fieldname
            if line[i:i+len(str_list[y])] == str_list[y] and line[i:i+len(str_list[y])] == line[i+len(str_list[y]):i+2*len(str_list[y])]:
                #seq_dict[str_list[y]] += 1
                cur_count += 1
            else:
                #Replace the value in Dict with Cur_count if exceed
                #To obtain only the largest count of consequtive repeat
                if cur_count > seq_dict[str_list[y]]:
                    seq_dict[str_list[y]] = cur_count
                    cur_count = 1