a, b, c = map(int, input().split())

if(c > b > a):
    print(a)
    print(b)
    print(c)
elif(b > a > c):
    print(c)
    print(a)
    print(b)
elif(a > c > b):
    print(b)
    print(c)
    print(a)
elif(c > a > b):
    print(b)
    print(a)
    print(c)
elif(b > c > a):
    print(a)
    print(c)
    print(b)
else:
    print(c)
    print(b)
    print(a)
print()
print(a)
print(b)
print(c)

