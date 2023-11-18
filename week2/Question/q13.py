N = int(input())

# 공백 처리
# 별 문제: 공백과 별들을 어떤 식을 활용해서 구현할 것인지
# 매번 생각해야 됨
for i in range(1, N + 1):
    print(' ' * (N-i) + '*' * i)
    
    