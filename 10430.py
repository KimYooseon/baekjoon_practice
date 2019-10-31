a,b,c = input().split()
A = int(a)
B = int(b)
C = int(c)

if A>=2 and B<=10000 and C<=10000:
    print((A+B)%C)
    print((A%C + B%C)%C)
    print((A*B)%C)
    print((A%C * B%C)%C)
