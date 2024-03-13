p1, c1, p2, c2 = map(int, input().split())

momento1 = p1 * c1
momento2 = p2 * c2

if momento1 == momento2:
    print('0')
elif momento1 > momento2:
    print('-1')
elif momento1 < momento2:
    print('1')