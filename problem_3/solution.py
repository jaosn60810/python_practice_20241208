# 第3題: 雞蛋大盜
n = int(input())
eggs = list(map(int, input().split()))
dp = [0] * (n + 1)
dp[1] = eggs[0]

for i in range(2, n + 1):
    dp[i] = max(dp[i - 1], dp[i - 2] + eggs[i - 1])

print(dp[n]) 