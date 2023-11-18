n = int(input()) # 라운드 수

# x : 창영, y : 상덕
x = y = 100

for _ in range(n):
    # a : 창영이 주사위 눈금, b : 상덕이 주사위눈금
    a, b = map(int, input().split())
    
    if a > b:
        y -= a
    elif a < b:
        x -= b
        
print(x)
print(y)
                
                
                