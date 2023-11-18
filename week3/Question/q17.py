T = int(input())
Y = K = 0 

# 테스트 케이스 하나당 9번 반복
for _ in range(T):
    for _ in range(9):
        y_score, k_score = map(int, input().split())
    
        Y += y_score # 누적
        K += k_score # 누적
    
if Y > K:
    print('Yonsei')
elif Y < K:
    print('Korea')
else:
    print('Draw')
    
    
    