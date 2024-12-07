# 第8題: 神秘符文之謎
n = int(input())
x = input()

if n % 2 == 0 and n % 3 != 0:
    print(x.upper() if x.islower() else x.lower() if x.isalpha() else int(x)**2)
elif n % 2 == 0 and n % 3 == 0:
    print(x)
elif n % 2 != 0 and n % 3 == 0:
    print(ord(x))
else:
    print(x * 2) 