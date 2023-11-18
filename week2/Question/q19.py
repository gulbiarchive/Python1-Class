N = int(input())

# 역순으로 반복
for i in range(N, 0, -1):
    print(' ' * (N-i) + '*'*((2*i)-1))
    
    
    