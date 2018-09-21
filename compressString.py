from itertools import groupby

string = input()
arr=[]
for k, g in groupby(string):
    arr.append(list(g))

for i in arr:
    print (len(i), int(i[0])),
