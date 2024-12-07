from collections import defaultdict
from math import gcd

# Input block
n = int(input())
points = [tuple(map(int, input().split(','))) for _ in range(n)]
points = list(set(points))

# Calculate the maximum number of collinear points
max_points = 0
for i in range(len(points)):
    slopes = defaultdict(int)
    duplicate = 1
    for j in range(len(points)):
        if i != j:
            dx = points[j][0] - points[i][0]
            dy = points[j][1] - points[i][1]
            if dx == 0 and dy == 0:
                duplicate += 1
            else:
                divisor = gcd(dx, dy)
                slope = (dx // divisor, dy // divisor)
                slopes[slope] += 1
    max_points = max(max_points, (max(slopes.values()) if slopes else 0) + duplicate)

# Print the result
print(max_points)
