# 第2題: 英雄好難
# 輸入資料
energy_values = list(map(int, input().split()))

# 初始化
n = len(energy_values)
max_sum = float('-inf')  # 改為負無窮大
best_subarray = []

# 暴力解法
for i in range(n):
    current_sum = 0
    for j in range(i, n):
        current_sum += energy_values[j]
        # 更新最大和和對應的子數組
        if current_sum > max_sum:
            max_sum = current_sum
            best_subarray = energy_values[i:j + 1]

print(f"子路徑為 {' '.join(map(str, best_subarray))} 且最大能量和為 {max_sum}")



