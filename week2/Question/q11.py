total = 0 # 합 저장할 변수

for i in range(5):
    score = int(input())
    if score < 40:
        score = 40 # 40 미만이면 항상 40점
    total += score # total 누적

print(total // 5) # 평균 출력(정수)


