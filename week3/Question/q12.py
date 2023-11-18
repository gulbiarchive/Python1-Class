V = int(input())
# 여러 개의 요소(문자열) 저장하기 위해 리스트 사용
vote = list(input())

A = B = 0

for i in vote:
    if i == 'A':
        A += 1 # 누적
    else:
        B += 1 # 누적
        
if A > B:
    print('A')
elif A < B:
    print('B')
else:
    print('Tie')
    
    