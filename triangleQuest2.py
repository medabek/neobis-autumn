from math import log10
n=int(input())
i = 1
while (n > log10(i)): 
    print(i**2); 
    i = i * 10 + 1
