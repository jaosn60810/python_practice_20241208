num = list(map(int,input().split()))
pos = []
neg = []
for i in num:
    if i < 0:
        neg.append(i)
    if i > 0:
        pos.append(i)
        
if len(neg)==0:
    print(f"子路徑為 {' '.join(map(str, pos))} 且最大能量和為 {sum(pos)}")
if len(pos)==0:
    print(f"子路徑為 {max(neg)} 且最大能量和為 {max(neg)}")
if len(pos)!=0 and len(neg)!=0:
    print(f"子路徑為 {max(pos)} 且最大能量和為 {max(pos)}")