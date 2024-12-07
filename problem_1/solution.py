# 第1題: 盼你早歸
target_name = input()
n = int(input())
names = [input() for _ in range(n)]
positions = [i + 1 for i, name in enumerate(names) if name == target_name]

if positions:
    print("\n".join(map(str, positions)))
else:
    print("None") 