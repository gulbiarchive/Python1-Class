N = int(input())

# 1 ~ 4
for i in range(1, N):
    print(' '*(N-i) + '*'*((2*i)-1))

# 5 ~ 9
for i in range(N, 0, -1):
    print(' ' * (N-i) + '*'*((2*i)-1))
    
    
    