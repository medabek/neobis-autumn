from collections import OrderedDict
dct = OrderedDict()
for i in range(int(input())):
    i = input()
    dct[i] = dct.get(i, 0) + 1
print(len(dct))
for w in dct.values():
    print(w, )
