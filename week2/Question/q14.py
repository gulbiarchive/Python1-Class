N = int(input())

# N부터 1까지 -1간격(역순)으로 이동하면서 반복
for i in range(N, 0, -1):
    print('*' * i)
    
    