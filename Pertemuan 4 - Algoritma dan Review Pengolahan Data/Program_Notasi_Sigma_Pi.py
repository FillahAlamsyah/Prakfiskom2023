print("Part 1".center(40,"-"))
s = 0

a = 1
b = 5

for i in range(a,b+1):
    print(i, end="\t")
    s = s+i
    print(s)

print("Part 2".center(40,"-"))

P = 1
a = 1
b = 5

for i in range(a,b+1):
    print(i, end="\t")
    P = P*i
    print(P)
