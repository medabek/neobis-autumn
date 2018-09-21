n=int(input())
z=1
x=int(n*(n+1)/2)
print(x)
for i in range(1,n+1):
    #print ((str(i) + " ") * i)
    print((i*(10**i-1))//9)
   
