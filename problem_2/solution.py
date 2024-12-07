# 第2題: 英雄好難
stones = list(map(int, input().split()))
max_sum = current_sum = stones[0]
start = end = temp_start = 0

for i in range(1, len(stones)):
    if stones[i] > current_sum + stones[i]:
        current_sum = stones[i]
        temp_start = i
    else:
        current_sum += stones[i]
    
    if current_sum > max_sum:
        max_sum = current_sum
        start = temp_start
        end = i

print(f"子路徑為 {' '.join(map(str, stones[start:end + 1]))} 且最大能量和為 {max_sum}") 