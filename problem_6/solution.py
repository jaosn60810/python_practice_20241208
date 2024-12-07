# 第6題: 剪刀、石頭、布
n = int(input())
for _ in range(n):
    p1, p2 = input().split()
    if p1 == p2:
        print(0)
    elif (p1 == 'Y' and p2 == 'P') or (p1 == 'P' and p2 == 'O') or (p1 == 'O' and p2 == 'Y'):
        print(1)
    else:
        print(2) 