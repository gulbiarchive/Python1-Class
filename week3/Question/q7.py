A, B = map(int, input().split())

if A % 2 == 0:
    print('짝수+', end = '')
else:
    print('홀수+', end = '')
    
if B % 2 == 0:
    print('짝수=', end = '')
else:
    print('홀수=', end = '')
    
if ((A+ B) % 2 == 0):
    print('짝수', end = '')
else:
    print('홀수', end = '')
    
print()


