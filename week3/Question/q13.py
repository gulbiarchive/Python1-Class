N = int(input())
cute = 0

for _ in range(N):
    # 각 사람의 의견 입력받기 
    if int(input()) == 1:
        cute += 1
    
    
if cute > N // 2:
    print('Junhee is cute!')
else:
    print('Junhee is not cute!')
    
    
    