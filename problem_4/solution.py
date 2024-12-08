from collections import defaultdict

# Input block
n = int(input())
points = [tuple(map(int, input().split(','))) for _ in range(n)]
points = list(set(points))  # 去除重複點

# Calculate the maximum number of collinear points
max_points = 1  # 初始化為1，因為至少有一個點
for i in range(len(points)):
    slopes = defaultdict(int)
    for j in range(i + 1, len(points)):  # 只需要檢查i之後的點
        dx = points[j][0] - points[i][0]
        dy = points[j][1] - points[i][1]
        
        if dx == 0:  # 垂直線的情況
            slope = float('inf')
        else:
            slope = dy / dx  # 使用浮點數斜率
        slopes[slope] += 1
    
        max_points = max(max_points, max(slopes.values()) + 1)  # +1 為當前點本身

# Print the result
print(max_points)