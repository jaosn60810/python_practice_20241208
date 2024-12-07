# 第9題: 尋找最大農作物收穫
a, b, c, d, e, t0, h0, t1, t2, h1, h2 = map(int, input().split())
max_p = float('-inf')
best_t = best_h = 0

for t in range(t1, t2 + 1):
    for h in range(h1, h2 + 1):
        p = a + b * t + c * h - d * (t - t0)**2 - e * (h - h0)**2
        if p > max_p or (p == max_p and t < best_t):
            max_p, best_t, best_h = p, t, h

print(best_t)
print(best_h)
print(max_p) 