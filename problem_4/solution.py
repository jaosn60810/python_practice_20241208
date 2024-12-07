# 第4題: 直線上最多的點數
from collections import defaultdict
from math import gcd

n = int(input())
points = [tuple(map(int, input().split(','))) for _ in range(n)]
max_points = 1

for i in range(n):
    slopes = defaultdict(int)
    for j in range(i + 1, n):
        dx, dy = points[j][0] - points[i][0], points[j][1] - points[i][1]
        g = gcd(dx, dy)
        slope = (dx // g, dy // g)
        slopes[slope] += 1
        max_points = max(max_points, slopes[slope] + 1)

print(max_points) 