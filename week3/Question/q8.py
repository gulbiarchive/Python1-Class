year, month, day = map(int, input().split())

# 복습
# 어떤 수를 10으로 나눈 나머지는 그 수의 일의 자리
if ((year - month + day) % 10 == 0):
    print('대박')
else:
    print('그럭저럭')
    
    