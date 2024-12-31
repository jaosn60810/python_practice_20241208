# 第3題: 雞蛋大盜
n = int(input())
eggs = list(map(int, input().split()))
# dp = [0] * (n + 1)
# dp[1] = eggs[0]

# for i in range(2, n + 1):
#     dp[i] = max(dp[i - 1], dp[i - 2] + eggs[i - 1])

# print(dp[n]) 


rob1, rob2 = 0, 0

# [rob1, rob2, n, n+1, ...]
for n in eggs:
    tmp = max(rob1 + n, rob2)
    rob1 = rob2
    rob2 = tmp
print(rob2)

# [1,2,3,1]
# n = 1
# tmp = max(rob1 + n, rob2) = max(0 + 1, 0) = 1
# rob1 = rob2 = 0
# rob2 = tmp = 1

# n = 2
# tmp = max(rob1 + n, rob2) = max(0 + 2, 1) = 2
# rob1 = rob2 = 1
# rob2 = tmp = 2

# n = 3
# tmp = max(rob1 + n, rob2) = max(1 + 3, 2) = 4
# rob1 = rob2 = 2
# rob2 = tmp = 4

# n = 1
# tmp = max(rob1 + n, rob2) = max(2 + 1, 4) = 4
# rob1 = rob2 = 4
# rob2 = tmp = 4