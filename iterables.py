from itertools import combinations
num=int(input("Enter the length: "))
arr=input("Enter the chars: ").split()
ran=int(input("Enter the range: "))
x=input("Probability of what: ")
arr=list(combinations(list(arr),ran))
#print(arr)
count=0
for i in arr:
    i=list(i)
    #print(i)
    for j in i:
        if j==x:
            count+=1
            break
print(count/len(arr))
