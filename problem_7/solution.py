# 第7題: 統計答案得分
n = int(input())
for _ in range(n):
    answers = input()
    score = current = 0
    for ans in answers:
        if ans == 'O':
            current += 1
            score += current
        else:
            current = 0
    print(score) 