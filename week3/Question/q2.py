n = int(input())

# 1 ~ n까지 반복
for i in range(1, n+1):
    # 3의 배수일 경우 출력 X
    if i % 3 == 0:
        continue
    print(i, end = ' ') # 가로 출력
# print()
# 출력 : 1 2 4 5 7 8 10 %    
# 이유
# print()는 자동으로 개행 문자 추가하는데 
# 현재 end 키워드로 줄바꿈 X
# 그러므로 마지막 줄에 개행 문자가 포함되지 않아서
# '%' 기호 등이 나타난다.


