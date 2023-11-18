while True:
    x, y = map(int, input().split())
    
    if x == 0 and y == 0:
        break
    
    if x < y and y % x == 0:
        print('factor') # 약수
    elif x > y and x % y == 0:
        print('multiple') # 배수
    else:
        print('neither')
        
        
        