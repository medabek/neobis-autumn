n = int(input())
m=int(input())

arrn=[]
arrA=[]
arrB=[]
count=0
for i in range(n):
    x=int(input())
    arrn.append(x)
#print(arrn)
for i in range(m):
    x=int(input())
    arrA.append(x)
#print(arrA)
for i in range(m):
    x=int(input())
    arrB.append(x)
#print(arrB)

for num in arrn:
    if num in arrA:
        count+=1
    elif num in arrB:
        count-=1
print (count)


