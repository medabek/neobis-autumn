import itertools
word = str(input())
arr = []
lenarr=[]
sortedarr=[]
for i in word:
    arr.append(i)
keys=[]
groups=[]

for k, g in itertools.groupby(arr):
    keys.append(k)
    groups.append(list(g))

for i in groups:
    lenarr.append(len(i))
#print(keys)
#print(groups)
#print(lenarr)
#print (max(groups, key=len))
listmy=sorted(groups)
#print(listmy)
for i in range(0,3):
    sortedarr.append(max(listmy, key=len))
    listmy.remove(max(listmy, key=len))
#print(sortedarr)
##def longest(l):
##    if(not isinstance(l, list)): return(0)
##    return(max([len(l),] + [len(subl) for subl in l if isinstance(subl, list)] +
##        [longest(subl) for subl in l]))
##print(longest(groups))
for i in range(len(sortedarr)):
    print(sortedarr[i][0], len(sortedarr[i]))
